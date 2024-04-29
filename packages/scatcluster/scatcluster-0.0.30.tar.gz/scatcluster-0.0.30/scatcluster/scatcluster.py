import json
from typing import List

from scatcluster.analysis.dendrogram import Dendrogram
from scatcluster.analysis.external_correlation import ExternalCorrelation
from scatcluster.analysis.predictions import Predictions
from scatcluster.analysis.processing import AnalysisProcessing
from scatcluster.analysis.waveform_correlations import WaveformCorrelations
from scatcluster.analysis.waveforms import Waveforms
from scatcluster.processing.ica import ICA
from scatcluster.processing.scattering import Scattering
from scatcluster.structure import Structure


def config_load(ssn_json_file: str, verbose=True):
    """Loads a ScatCluster configuration and returns a ScatCluster instance.

    Args:
        ssn_json_file (str): The location of the ScatCluster Configuration json file

    Returns:
        _type_: A preloaded ScatCluster instance.
    """
    with open(ssn_json_file, 'r', encoding='utf8') as jsonfile:
        sc_config = json.load(jsonfile)
    SC = ScatCluster(**sc_config)
    if verbose:
        print('ScatCluster config loaded:')
        print(json.dumps(sc_config, indent=2))
    return SC


class ScatCluster(Structure, Scattering, ICA, Dendrogram, Waveforms, Predictions, ExternalCorrelation,
                  WaveformCorrelations, AnalysisProcessing):
    """INGV ScatCluster class workflow for clustering continuous time series with a deep scattering network.
    """

    def __init__(self,
                 data_savepath: str,
                 data_client_path: str,
                 data_network: str,
                 data_station: str,
                 data_location: str,
                 data_channel: str,
                 data_sample_starttime: str,
                 data_sample_endtime: str,
                 data_starttime: str,
                 data_endtime: str,
                 sc_config=None,
                 data_exclude_days: List[str] = [],
                 network_segment: int = 3600,
                 network_step: int = 3600,
                 network_sampling_rate: int = 50,
                 network_banks: tuple = ({
                     'octaves': 4,
                     'resolution': 4,
                     'quality': 2
                 }, {
                     'octaves': 7,
                     'resolution': 1,
                     'quality': 1
                 }),
                 network_pooling: str = 'avg',
                 ica_ev_limit: float = 0.99,
                 ica_min_ICAs: int = 10,
                 ica_max_ICAs: int = 10,
                 ica_overwrite_previous_models: bool = False,
                 ica_explained_variance_score: float = None,
                 dendrogram_method: str = 'ward',
                 dendrogram_time_zone: str = None,
                 waveforms_n_samples: int = 5,
                 waveforms=None,
                 spectrograms=None):

        self.sc_config = sc_config
        self.data_savepath = data_savepath
        self.data_client_path = data_client_path
        self.data_network = data_network
        self.data_station = data_station
        self.data_location = data_location
        self.data_channel = data_channel
        self.data_sample_starttime = data_sample_starttime
        self.data_sample_endtime = data_sample_endtime
        self.data_starttime = data_starttime
        self.data_endtime = data_endtime
        self.data_exclude_days = data_exclude_days
        self.data_day_list = None
        self.sample_stream = None
        self.sample_times = None
        self.sample_data = None
        self.sample_data_segments = None
        self.sample_times_scatterings = None
        self.sample_scattering_coefficients = None
        self.data_times = None
        self.data_stream = None
        self.data_all = None
        self.channel_list = None
        self.data_scat_coef_vectorized = None
        self.network_segment = network_segment
        self.network_step = network_step
        self.network_sampling_rate = network_sampling_rate
        self.network_banks = network_banks
        self.network_pooling = network_pooling
        self.network_samples_per_segment = None
        self.network_samples_per_step = None
        self.net = None
        self.ica_ev_limit = ica_ev_limit
        self.ica_min_ICAs = ica_min_ICAs
        self.ica_max_ICAs = ica_max_ICAs
        self.ica_overwrite_previous_models = ica_overwrite_previous_models
        self.ica_median_filter = 31
        self.ica = None
        self.ica_features = None
        self.ica_explained_variance_score = None
        self.dendrogram_method = dendrogram_method
        self.dendrogram_linkage = None
        self.dendrogram_predictions = None
        self.dendrogram_timestamps = None
        self.dendrogram_linkage = None
        self.dendrogram_time_zone = None
        self.waveforms_n_samples = waveforms_n_samples
        self.network_banks_name = '_'.join([str(order[vals]) for order in self.network_banks for vals in order.keys()])
        self.network_name = f'{self.network_segment}_{self.network_step}_{self.network_sampling_rate}_{self.network_banks_name}_{self.network_pooling}'
        self.waveforms = None
        self.spectrograms = None

    def __setitem__(self, key, value):
        setattr(self, key, value)
