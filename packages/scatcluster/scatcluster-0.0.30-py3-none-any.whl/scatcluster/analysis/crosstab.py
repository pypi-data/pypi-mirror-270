import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes
from scipy.cluster import hierarchy
from sklearn.metrics import fowlkes_mallows_score

from scatcluster.helper import COLORS


class SSNCrossTabAnalysis:
    """ScatCluster Add-on to run cross-analysis of different clusterings
    """

    def __init__(
        self,
        data_savepath: str = '/home/jovyan/shared/users/zerafa/data/sds.chris/scatcluster-sds/',
        data_network: str = 'ET',
        data_station: str = 'SOE0',
        data_location: str = '',
        network_sampling_rate_banks_pooling: str = '50_4_4_2_7_1_1_avg',
        ica_number: int = 10,
    ):
        self.data_savepath = data_savepath
        self.data_network = data_network
        self.data_station = data_station
        self.data_location = data_location
        self.network_sampling_rate_banks_pooling = network_sampling_rate_banks_pooling
        self.ica_number = ica_number

    def _get_predictions(self, win_size, num_clusters):
        file_path = f'{self.data_savepath}clustering/{self.data_network}_{self.data_station}_{self.data_location}_{win_size}_{win_size}_{self.network_sampling_rate_banks_pooling}_ICA_{self.ica_number}_clusters_{num_clusters}.npz'
        return np.load(file_path)['predictions']

    def _build_crosstab_data(self,
                             cluster_1=3600,
                             num_clusters_1=10,
                             cluster_2=60,
                             num_clusters_2=10,
                             normalization=None):
        preds_1 = self._get_predictions(cluster_1, num_clusters_1)
        preds_2 = self._get_predictions(cluster_2, num_clusters_2)
        factor_difference = int(len(preds_2) / len(preds_1))

        print(
            f'Factor difference between predictions "{cluster_1}s window, {num_clusters_1} clusters" and "{cluster_2}s window, {num_clusters_2} clusters" : {factor_difference} \n'
        )

        preds_1_modified = np.repeat(preds_1, factor_difference)

        df_preds = pd.DataFrame({'predictions_1': preds_1_modified, 'predictions_2': preds_2})

        _normalization_options = ('all', 'index', 'columns')
        if normalization is None:
            ct_data = pd.crosstab(df_preds.predictions_1, df_preds.predictions_2)
        elif normalization in _normalization_options:
            ct_data = pd.crosstab(df_preds.predictions_1, df_preds.predictions_2, normalize=normalization)
            ct_data = ct_data * 100
        else:
            raise ValueError(
                f"Provided Normalization is not valid. This can be 'None' or [{_normalization_options}]. Kindly see https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html for more info."
            )
        ct_data = ct_data.sort_index(ascending=False)
        return ct_data, factor_difference, fowlkes_mallows_score(df_preds.predictions_1, df_preds.predictions_2)

    def plot_clustering_crosstab(self,
                                 cluster_1=3600,
                                 num_clusters_1=10,
                                 cluster_2=60,
                                 num_clusters_2=10,
                                 normalization=None,
                                 **kwargs):

        ct_data, _, fws = self._build_crosstab_data(cluster_1, num_clusters_1, cluster_2, num_clusters_2, normalization)

        fig, ax = plt.subplots(figsize=(7, 7), **kwargs)
        _fmt = '.0f'
        if normalization is not None:
            _fmt = '.1f'
        s = sns.heatmap(ct_data, cmap='YlGnBu', annot=True, cbar=False, fmt=_fmt, linewidth=.5, ax=ax)
        _norm_title = ''
        if normalization is not None:
            for t in s.texts:
                t.set_text(t.get_text() + ' %')
            _norm_title = f'\nNormalization: {normalization}'
        ax.set_xlabel(f'{cluster_2}s window, {num_clusters_2} clusters')
        ax.set_ylabel(f'{cluster_1}s window, {num_clusters_1} clusters')
        ax.set_title('Comparison of Clusterings Predictions\nFWS similarity {:.2f}%{}'.format(fws * 100, _norm_title))
        ax.xaxis.set_ticks_position('top')
        ax.xaxis.set_label_position('top')

        _norm_fname = ''
        if normalization is not None:
            _norm_fname = f'_Normalization_{normalization}'
        plt.savefig(
            f'{self.data_savepath}figures/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_sampling_rate_banks_pooling}_ICA_{self.ica_number}_crosstab_{_norm_fname}_{cluster_1}_{num_clusters_1}_{cluster_2}_{num_clusters_2}.png'
        )

    def _custom_dendrogram_crosstab(self, linkage: np.array, ax: Axes, depth: int = 30, orientation='left', factor=1):
        # Show and get dendrogram
        with plt.rc_context({'lines.linewidth': 0.7}):
            dendrogram_infos = hierarchy.dendrogram(linkage,
                                                    p=depth,
                                                    truncate_mode='lastp',
                                                    color_threshold=0,
                                                    ax=ax,
                                                    orientation=orientation,
                                                    above_threshold_color='0.3',
                                                    count_sort=True,
                                                    labels=None,
                                                    show_leaf_counts=False)

            R = hierarchy.dendrogram(
                linkage,
                p=depth,
                truncate_mode='lastp',
                color_threshold=0,
                no_plot=True,
                orientation=orientation,
                above_threshold_color='0.3',
                count_sort=True,
                labels=None,
            )

        # Extract informations
        coordinates, _ = get_leaves(dendrogram_infos, ax)

        # leave population
        pops = [x for x in R['ivl']]

        # Plot leave nodes
        node_style = dict(ms=5, mec='0.3', mew=0.7, clip_on=False)
        for coordinate, color, pop in zip(coordinates, COLORS, pops):
            if orientation == 'left':
                ax.plot(0, coordinate, 'o', mfc=color, **node_style)
                index = int((coordinate - 5) / 10) + 1
                label = '{:d}\n{}\n{}'.format(index, pop,
                                              '[' + str(int(pop.replace('(', '').replace(')', '')) * factor) + ']')
                ax.text(-0.1, coordinate, label, color=color, va='center')
            if orientation == 'bottom':
                ax.plot(coordinate, 0, 'o', mfc=color, **node_style)
                index = int((coordinate - 5) / 10) + 1
                label = '{:d}\n{}'.format(index, pop)
                ax.text(coordinate, -0.1, label, color=color, ha='center')

    def _get_linkage(self, win_size):
        return np.load(
            f'{self.data_savepath}clustering/{self.data_network}_{self.data_station}_{self.data_location}_{win_size}_{win_size}_{self.network_sampling_rate_banks_pooling}_linkage.npy'
        )

    def plot_crosstab_dendrograms(self,
                                  cluster_1=3600,
                                  num_clusters_1=10,
                                  cluster_2=60,
                                  num_clusters_2=10,
                                  normalization=None,
                                  **kwargs):

        ct_data, factor, fws = self._build_crosstab_data(cluster_1, num_clusters_1, cluster_2, num_clusters_2,
                                                         normalization)

        f, ax = plt.subplots(2,
                             2,
                             gridspec_kw={
                                 'width_ratios': [1, 8],
                                 'height_ratios': [8, 1]
                             },
                             figsize=(8, 8),
                             **kwargs)
        _fmt = '.0f'
        if normalization is not None:
            _fmt = '.1f'
        s = sns.heatmap(ct_data, cmap='YlGnBu', annot=True, cbar=False, fmt=_fmt, linewidth=.5, ax=ax[0, 1])
        _norm_title = ''
        if normalization is not None:
            for t in s.texts:
                t.set_text(t.get_text() + ' %')
            _norm_title = f'\nNormalization: {normalization}'
        ax[0, 1].set_xlabel(f'{cluster_2}s window, {num_clusters_2} clusters')
        ax[0, 1].set_ylabel(f'{cluster_1}s window, {num_clusters_1} clusters')
        ax[0, 1].set_title('Comparison of Clusterings Predictions\nFWS similarity {:.2f}%{}'.format(
            fws * 100, _norm_title))
        ax[0, 1].xaxis.set_ticks_position('top')
        ax[0, 1].xaxis.set_label_position('top')
        ax[0, 1].yaxis.set_ticks_position('right')
        ax[0, 1].yaxis.set_label_position('right')

        linkage_1 = self._get_linkage(win_size=cluster_1)
        self._custom_dendrogram_crosstab(linkage=linkage_1, ax=ax[0, 0], depth=num_clusters_1, factor=factor)
        linkage_2 = self._get_linkage(win_size=cluster_2)
        self._custom_dendrogram_crosstab(linkage=linkage_2, ax=ax[1, 1], depth=num_clusters_2, orientation='bottom')

        ax[1, 0].set_axis_off()
        _norm_fname = ''
        if normalization is not None:
            _norm_fname = f'_Normalization_{normalization}'
        plt.savefig(
            f'{self.data_savepath}figures/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_sampling_rate_banks_pooling}_ICA_{self.ica_number}_crosstab_dendrogram_{_norm_fname}_{cluster_1}_{num_clusters_1}_{cluster_2}_{num_clusters_2}.png'
        )
