import os
import pickle
from glob import glob
from typing import Optional

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import dates as mdates
from obspy.core import UTCDateTime
from scipy.signal import medfilt
from sklearn.decomposition import FastICA
from sklearn.metrics import explained_variance_score, mean_squared_error
from sklearn.preprocessing import RobustScaler

from scatcluster.helper import demad, list_of_strings


def round_nearest(x, a):
    return round(x / a) * a


class ICA:

    def _get_index_from_UTC_timestamp(self, utc_timestamp: str):
        df_time = pd.DataFrame({'time': self.data_times})
        return max(df_time.loc[
            df_time['time'] < mdates.date2num(UTCDateTime(utc_timestamp)),
        ].index)

    def process_ICA_single(self,
                           num_ICA: int,
                           return_data: bool = False,
                           exclude_timestamps: Optional[list[str]] = None,
                           exclude_timestamps_skip: int = 5,
                           **kwargs):
        """Process the data for a single run of ICA. This will reduce to a dataset of dimension num_ICA.

        Args:
            num_ICA (int): The number of dimensions to be reduced to.
            return_data (bool, optional): Toggle to determine if the data should be returned as part of the function call. Defaults to False.

        Returns:
            _type_: _description_
        """
        print(f'Performing ICA for {num_ICA} ICAs')
        ica_model_path = f'{self.data_savepath}ICA/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_dimension_{num_ICA}.pickle'
        # check if reduction exists already
        if (os.path.exists(ica_model_path) and self.ica_overwrite_previous_models is False):
            print('  Using pre-calculated model')
            model = pickle.load(open(ica_model_path, 'rb'))
        else:
            # else fit
            kwargs['max_iter'] = 1000 if kwargs.get('max_iter') is None else kwargs.get('max_iter')
            kwargs['whiten'] = 'unit-variance' if kwargs.get('whiten') is None else kwargs.get('whiten')
            model = FastICA(n_components=num_ICA, random_state=42, **kwargs)

        # SCALING
        print('RobustScaling of data before fitting ICA')
        # Exclude any timestamps
        scat_coeff_data = self.data_scat_coef_vectorized.copy()
        if exclude_timestamps is not None:
            for ts in exclude_timestamps:
                print(
                    f'Timestamp {UTCDateTime(ts)} - {UTCDateTime(ts) + (self.network_segment * exclude_timestamps_skip)} has been excluded from the Scaling fit and Model fit.'
                )
                ts_index = self._get_index_from_UTC_timestamp(ts)
                scat_coeff_data = np.delete(scat_coeff_data, np.s_[ts_index:ts_index + exclude_timestamps_skip], 0)

        scaler = RobustScaler()
        # fit on subset
        scaler.fit(scat_coeff_data)
        # Transform on full data
        scat_coeff_data_scaled = scaler.transform(self.data_scat_coef_vectorized.copy())

        print('Fitting and transforming the data for FastICA')
        # fit on a subset of data
        model.fit(scaler.transform(scat_coeff_data))
        # Transform on full data
        features = model.transform(scat_coeff_data_scaled)

        features_inverse = model.inverse_transform(features)
        score_exp_var = explained_variance_score(scat_coeff_data_scaled, features_inverse)
        score_mse = mean_squared_error(scat_coeff_data_scaled, features_inverse)
        print(f'      ICAs #{num_ICA} : Explained Variance {score_exp_var * 100:0.5f}% : MSE {score_mse:0.5f}')

        self.ica = model
        self.ica_number_components = num_ICA
        self.ica_features = features
        self.ica_explained_variance_score = score_exp_var

        # SAVE ICA MODEL IN PICKLE FILE
        with open(ica_model_path, 'wb') as handle:
            pickle.dump(model, handle, protocol=pickle.HIGHEST_PROTOCOL)

        # save the features
        np.savez(
            f'{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_features_{num_ICA}.npz',
            features=features,
            features_inverse=features_inverse,
            score_explained_variance=score_exp_var,
            score_mse=score_mse)

        if return_data:
            return score_exp_var, score_mse, model, features

    def process_ICA_range(self,
                          exclude_timestamps: Optional[list[str]] = None,
                          exclude_timestamps_skip: int = 3,
                          **kwargs) -> None:
        """Process ICA dimension reduction for a range of possible dimensions controlled via ica_min_ICAs, ica_max_ICAs and ica_ev_limit.
        """
        score_exp_var = 0
        ica_min_ICAs = 6 if self.ica_min_ICAs is None else self.ica_min_ICAs
        ica_max_ICAs = 20 if self.ica_max_ICAs is None else self.ica_max_ICAs
        num_ICA = ica_min_ICAs - 1
        while (score_exp_var <= self.ica_ev_limit and num_ICA < ica_max_ICAs):
            num_ICA += 1
            score_exp_var, _, model, features = self.process_ICA_single(num_ICA=num_ICA,
                                                                        return_data=True,
                                                                        exclude_timestamps=exclude_timestamps,
                                                                        exclude_timestamps_skip=exclude_timestamps_skip,
                                                                        **kwargs)
        if num_ICA == ica_max_ICAs:
            print(
                f'Failed to reach an explained variance of {self.ica_ev_limit* 100:0.5f} with a max number of {self.ica_max_ICAs} ICAs. Either increase the maximum number of ICAs or decrease the Explained Variance Limit.'
            )
        else:
            print(f'Recommended number of ICAs {num_ICA}.\nThe Explained Variance with these ICAs is {score_exp_var}.')

        self.ica = model
        self.ica_number_components = num_ICA
        self.ica_features = features
        print(f'Compressed Vectorised Scat. Coefficients Array after ICA : {features.shape}')

    def preload_ICA(self, num_ICA: int) -> None:
        """Load a pre-calculated ICA and set required variables

        Args:
            num_ICA (int): Desired number of ICAs
        """
        if not os.path.exists(
                f'{self.data_savepath}ICA/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_dimension_{num_ICA}.pickle'
        ):
            raise ValueError(
                f"The supplied number of ICAs {num_ICA} has not been computed. Choose another number for the ICAs or calcate using 'process_ICA_single'"
            )

        self.ica = pickle.load(
            open(
                f'{self.data_savepath}ICA/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_dimension_{num_ICA}.pickle',
                'rb'))

        ica_results = np.load(
            f'{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_features_{num_ICA}.npz'
        )
        self.ica_features = ica_results['features']
        self.ica_features_inverse = ica_results['features_inverse']
        self.ica_explained_variance_score = ica_results['score_explained_variance']
        self.ica_mse = ica_results['score_mse']

        self.ica_number_components = num_ICA

        print(f'Compressed Vectorised Scat. Coefficients Array after ICA : {self.ica_features.shape}')

        self.data_times = np.load(
            f'{self.data_savepath}data/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_times.npy'
        )

    def plot_ICA(self, **kwargs) -> None:
        """Visualise the ICAs
        """
        dimensions = self.ica_features.shape[1]
        # Preprocess
        features = self.ica_features.T
        features = demad(features)

        # features = latents
        FACTOR = 0.5

        # Show in time
        n_features, _ = features.shape

        # Figure
        kwargs['figsize'] = (10, 7) if kwargs.get('figsize') is None else kwargs.get('figsize')
        _, ax = plt.subplots(1, **kwargs)

        # Show
        for index, feature in enumerate(features.copy()):
            color = f'C{index % 3}'
            feature *= 0.5
            feature += index + 1
            feature_filtered = medfilt(
                feature, self.ica_median_filter if self.ica_median_filter is not None else
                (int(3600 / self.network_segment) * 3) + 1)
            ax.plot(self.data_times, feature, '.', ms=3, alpha=0.5, mew=0, color=color)
            ax.plot(self.data_times, feature_filtered, lw=0.7, color='k')

        # Labels
        ax.grid()
        ax.set_ylim(0, n_features + FACTOR)
        ax.set_yticks(np.arange(n_features) + 1)
        ax.set_yticklabels(list_of_strings(n_features))
        ax.set_ylabel('Independant component index')

        # Date labels
        dateticks = mdates.AutoDateLocator()
        datelabels = mdates.ConciseDateFormatter(dateticks)
        ax.xaxis.set_major_locator(dateticks)
        ax.xaxis.set_major_formatter(datelabels)
        ax.set_xlim(self.data_times.min(), self.data_times.max())

        # Remove borders
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.tick_params(axis='y', length=0)
        plt.title(
            f'{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_ICAs_{dimensions}\n{dimensions} ICAs - Explained Variance : {self.ica_explained_variance_score*100:0.5f}'
        )

        plt.savefig(
            f'{self.data_savepath}figures/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_ICAs_{dimensions}.png'
        )

        plt.show()

    def plot_ICA_zoom(self, ICA_letter: str, zoom_time_start: str, zoom_time_end: str, **kwargs) -> None:
        """Visualise a zoomed section of an ICA

        Args:
            ICA_letter (str): ICA letter
            zoom_time_start (str): Zoom section start
            zoom_time_end (str): Zoom section end
        """
        ica_number = [
            x_enum for x_enum, x in enumerate(list_of_strings(self.ica.n_components)) if x == ICA_letter.upper()
        ][0]

        features = self.ica_features.T
        features_smoothed = demad(features)
        # Zoom into an ICA
        kwargs['figsize'] = (10, 7) if kwargs.get('figsize') is None else kwargs.get('figsize')
        _, ax = plt.subplots(**kwargs)
        ax.plot(self.data_times, features[ica_number], '.', ms=3, alpha=0.5, mew=0)
        ax.plot(self.data_times, features_smoothed[ica_number], lw=0.7, color='k')
        ax.set_xlim(min(self.data_times[self.data_times > int(mdates.date2num(UTCDateTime(zoom_time_start)))]),
                    min(self.data_times[self.data_times > int(mdates.date2num(UTCDateTime(zoom_time_end)))]))
        ax.set_ylim(-2, 2)
        ax.grid()
        locator = mdates.AutoDateLocator()
        formatter = mdates.ConciseDateFormatter(locator)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)

        plt.savefig(
            f'{self.data_savepath}figures/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_ICAs_{self.ica.n_components}_{ICA_letter}_Zoom_{zoom_time_start}_{zoom_time_end}.png'
        )

        plt.show()

    def plot_ica_contribution(self, **kwargs) -> None:
        """Visualise the ICA contribution to each cluster
        """

        # Calculate centroid
        classes = np.unique(self.dendrogram_predictions)
        feature_usage = np.zeros((self.ica_features.shape[1], len(classes)))

        for cluster in classes:
            within_cluster = self.dendrogram_predictions == cluster
            cluster_samples = self.ica_features[within_cluster]
            contributions = np.mean(cluster_samples, axis=0)
            contributions /= np.abs(contributions).sum()
            feature_usage[:, cluster - 1] = contributions

        vmax = round_nearest(np.abs(feature_usage).max(), 0.05)
        cmap = plt.cm.RdYlBu
        bounds = np.arange(-vmax, vmax, .05)
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

        kwargs['figsize'] = (8, 5) if kwargs.get('figsize') is None else kwargs.get('figsize')
        _, ax = plt.subplots(1, 1, **kwargs)
        img = ax.matshow(feature_usage, cmap=cmap, norm=norm)

        cb = plt.colorbar(img, orientation='horizontal')
        cb.minorticks_on()
        cb.set_label('Normalised contribution')
        ax.set_title('Contribution of ICA to prediction\nCluster')
        ax.set_ylabel('ICA component')
        ax.set_xticks(range(len(classes)), range(1, len(classes) + 1))
        ax.set_yticks(range(self.ica_features.shape[1]), list_of_strings(self.ica_features.shape[1]))

        plt.savefig(
            f'{self.data_savepath}figures/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_ICA_{self.ica.n_components}_clustering_{self.ica.n_components}_Waveform_contribution.png',
            bbox_inches='tight')

        plt.show()

    def list_linkages(self):
        print(
            glob(
                f'{self.data_savepath}clustering/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_ICA_*linkage*'
            ))
