import json
import os
from glob import glob
from typing import List


class Structure:

    def prepare_directory_structure(
            self,
            directories: List[str] = ['scatterings', 'figures', 'networks', 'ICA', 'clustering', 'data',
                                      'config']) -> None:
        """Build directory structure required for workflow processing

        Args:
            directories (List[str], optional): Directories created as part of the workflow. Defaults to ['scatterings', 'figures', 'networks', 'ICA','clustering','data'].
        """
        if self.data_savepath == '':
            raise ValueError('"data_savepath" has not been set up correctly. Kindly update the parametrization.')

        if os.path.exists(self.data_savepath):
            print(f'Main directory {self.data_savepath} already exists. \n')
        else:
            os.mkdir(self.data_savepath)
            print(f'Main directory {self.data_savepath} created. \n')

        for path in directories:
            isExist = os.path.exists(f'{self.data_savepath}{path}')
            if not isExist:
                os.makedirs(f'{self.data_savepath}{path}')
                print(f'Directory {self.data_savepath}{path} created.')
            else:
                print(f'Directory {self.data_savepath}{path} already exists.')

    def delete_scatterings(self) -> None:
        file_list_scatterings = glob(
            f'{self.data_savepath}scatterings/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}_scatterings_*.npz'
        )
        for file in file_list_scatterings:
            os.remove(file)
        print(f'{len(file_list_scatterings)} scatterings have been deleted from "{self.data_savepath}scatterings/"\n')

    def config_store(self):
        sc_config = {
            'data_savepath': self.data_savepath,
            'data_client_path': self.data_client_path,
            'data_network': self.data_network,
            'data_station': self.data_station,
            'data_location': self.data_location,
            'data_channel': self.data_channel,
            'data_sample_starttime': self.data_sample_starttime,
            'data_sample_endtime': self.data_sample_endtime,
            'data_starttime': self.data_starttime,
            'data_endtime': self.data_endtime,
            'data_exclude_days': self.data_exclude_days,
            'network_segment': self.network_segment,
            'network_step': self.network_step,
            'network_sampling_rate': self.network_sampling_rate,
            'network_banks': self.network_banks,
            'network_pooling': self.network_pooling,
            'ica_ev_limit': self.ica_ev_limit,
            'ica_min_ICAs': self.ica_min_ICAs,
            'ica_max_ICAs': self.ica_max_ICAs,
            'ica_overwrite_previous_models': self.ica_overwrite_previous_models,
            'dendrogram_method': self.dendrogram_method,
            'waveforms_n_samples': self.waveforms_n_samples
        }

        ssn_json_file = f'{self.data_savepath}config/{self.data_network}_{self.data_station}_{self.data_location}_{self.network_name}.json'

        with open(ssn_json_file, 'w', encoding='utf8') as jsonfile:
            json.dump(sc_config, jsonfile)

        print(f'SSN config stored at "{ssn_json_file}"')

    def config_show(self):
        print(self.__dict__)
