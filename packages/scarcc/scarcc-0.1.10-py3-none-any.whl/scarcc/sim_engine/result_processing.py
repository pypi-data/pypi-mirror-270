import re
from dataclasses import dataclass
from typing import Dict, Union, List
import pandas as pd

from scarcc.data_analysis.flux.flux_snapshot import adjust_flux_df
from scarcc.data_analysis import get_desired_cycle
from scarcc.utils import convert_arg_to_list

@dataclass
class SimObjectBase:
    # checkerboard handled in adjust_flux_df automatically
    E0: 'cobra.Model'
    S0: 'cobra.Model'
    sim_object: 'comets.solution'
    alpha_table: pd.DataFrame
    current_gene: str

    def __post_init__(self):
        if isinstance(self.current_gene, list):
            self.current_gene = '.'.join(self.current_gene)
        self.biomass_df = (self.sim_object.total_biomass.set_index('cycle'))
        self.model_dict = {'E0': self.E0, 'S0': self.S0}
        self.species_list = [self.model_dict[ele] for ele in self.biomass_df.columns]
        self.culture = 'coculture' if len(self.species_list)>1 else f'monoculture'
        self.biomass_df = self.biomass_df.add_suffix(f'_{self.current_gene}_{self.culture}') # ?need to use rename_columns?

def get_flux_snapshot(sob: SimObjectBase, model: 'cobra.Model' = None): # to map
    model_id = model.id
    biomass_df = sob.biomass_df.filter(regex=f'{model_id}') # suffix already added
    flux_df = sob.sim_object.fluxes_by_species[f'{model_id}'].copy()
    flux_df['Species'] = model_id
    flux_df['culture'] = sob.culture
    flux_df['Gene_inhibition'] = sob.current_gene
    flux_df = adjust_flux_df(model, flux_df, sob.current_gene, alpha_table=sob.alpha_table)
    
    # get the last cycle
    desired_cycle = get_desired_cycle(biomass_df)
    # return desired_cycle
    # TODO: snapshot handler
    snap_shot_cycle = int(desired_cycle.cycle_max_gr)
    snap_shot = flux_df.query('cycle == @snap_shot_cycle')
    return snap_shot

def extract_biomass_flux_df(E0: 'cobra.Model', S0: 'cobra.Model', sim_object_list: List['comets.solution'], alpha_table: pd.DataFrame, current_gene: str):
    # function for construct class and extraction
    def extract_biomass_flux_df_per_sim(sob: SimObjectBase) -> Dict[str, Union[pd.DataFrame, List]]: # list concat all together altogether for efficiency
        # this is the output to the get_BM_df function
        biomass_flux_dict = dict()
        biomass_flux_dict['biomass'] = sob.biomass_df
        # biomass_flux_dict['flux'] = pd.concat([get_flux_snapshot(sob, model_id=ele) for ele in sob.species_list])
        biomass_flux_dict['flux'] = [get_flux_snapshot(sob, model=ele) for ele in sob.species_list]
        return biomass_flux_dict['biomass'], biomass_flux_dict['flux']
    
    def construct_sob(sim_object: 'comets.solution'):
        return SimObjectBase(E0=E0, S0=S0, sim_object=sim_object, alpha_table=alpha_table, current_gene=current_gene)
    
    # zip(biomass_df_list, flux_df_list)
    return zip(*[extract_biomass_flux_df_per_sim(construct_sob(sim_object)) for sim_object in convert_arg_to_list(sim_object_list)])

def rename_columns(df):
    df.columns = [re.sub('S0_ac_','S0.ac_', ele) for ele in df] # S0_ac -> S0.ac
    df.columns = [re.sub('S0_gal_','S0.gal_', ele) for ele in df] # S0_ac -> S0.ac
    df.columns = [re.sub(',','.',
           re.sub('\'|\(|\)| |\[|\]','',ele)) # ('gene1', 'gene2') -> gene1.gene2
           for ele in df.columns]
    return(df.columns)
    
def gene_index_culture_col_df(analysis_df): 
    analysis_df['Gene_inhibition'] =  ['.'.join(map(str, convert_arg_to_list(l))) for l in analysis_df.Gene_inhibition] # SG, DG, checkerboard g1.g2 form
    analysis_df = analysis_df.set_index('Gene_inhibition')
    return analysis_df
