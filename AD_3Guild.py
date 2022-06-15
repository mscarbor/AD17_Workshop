from cobra import Model, Reaction, Metabolite
import cobra
import xlsxwriter

model = Model('model')

########################################################################################################################
########################################################################################################################

# GFOs !!
pyr_GFOc = Metabolite('pyr_GFOc', formula='C3H3O3', name='Pyruvate', compartment='GFOc', charge=-1)
amp_GFOc = Metabolite('amp_GFOc', formula='C10H12N5O7P', name='AMP', compartment='GFOc', charge=-2)
cit_GFOc = Metabolite('cit_GFOc', formula='C6H5O7', name='Citrate', compartment='GFOc', charge=-3)
oaa_GFOc = Metabolite('oaa_GFOc', formula='C4H2O5', name='Oxaloacetate', compartment='GFOc', charge=-2)
_6pgl_GFOc = Metabolite('_6pgl_GFOc', formula='C6H9O9P', name='6-phospho-D-glucono-1,5-lactone', compartment='GFOc',charge=-2)
nadp_GFOc = Metabolite('nadp_GFOc', formula='C21H25N7O17P3', name='Nicotinamide adenine dinucleotide phosphate',compartment='GFOc', charge=-3)
nadph_GFOc = Metabolite('nadph_GFOc', formula='C21H26N7O17P3',name='Nicotinamide adenine dinucleotide phosphate - reduced', compartment='GFOc', charge=-4)
glx_GFOc = Metabolite('glx_GFOc', formula='C2HO3', name='Glyoxylate', compartment='CELLc', charge=-1)
fum_GFOc = Metabolite('fum_GFOc', formula='C4H2O4', name='Fumarate', compartment='GFOc', charge=-2)
mal__L_GFOc = Metabolite('mal__L_GFOc', formula='C4H4O5', name='L-Malate', compartment='GFOc', charge=-2)
fad_GFOc = Metabolite('fad_GFOc', formula='C27H31N9O15P2', name='Flavin adenine dinucleotide oxidized',compartment='GFOc', charge=-2)
fadh2_GFOc = Metabolite('fadh2_GFOc', formula='C27H33N9O15P2', name='Flavin adenine dinucleotide reduced',compartment='GFOc', charge=-2)
succ_GFOc = Metabolite('succ_GFOc', formula='C4H4O4', name='Succinate', compartment='GFOc', charge=-2)
succoa_GFOc = Metabolite('succoa_GFOc', formula='C25H35N7O19P3S', name='Succinyl-CoA', compartment='GFOc', charge=-5)
akg_GFOc = Metabolite('akg_GFOc', formula='C5H4O5', name='2-Oxoglutarate', compartment='GFOc', charge=-2)
icit_GFOc = Metabolite('icit_GFOc', formula='C6H5O7', name='Isocitrate', compartment='GFOc', charge=-3)
pep_GFOc = Metabolite('pep_GFOc', formula='C3H2O6P', name='Phosphoenolpyruvate', compartment='GFOc', charge=-3)
h2o_GFOc = Metabolite('h2o_GFOc', formula='H2O', name='H2O', compartment='GFOc', charge=0)
glc__D_GFOc = Metabolite('glc__D_GFOc', formula='C6H12O6', name='D-Glucose', compartment='GFOc', charge=0)
g6p__B_GFOc = Metabolite('g6p__B_GFOc', formula='C6H11O9P', name='B-Glucose-6-P', compartment='GFOc', charge=-2)
biomass_GFOc = Metabolite('biomass_GFOc', formula='', name='Biomass', compartment='GFOc', charge=0)
nh4_GFOc = Metabolite('nh4_GFOc', formula='NH4', name='Ammonium', compartment='GFOc', charge=1)
so4_GFOc = Metabolite('so4_GFOc', formula='O4S', name='Sulfate', compartment='GFOc', charge=-2)
for_GFOc = Metabolite('for_GFOc', formula='CHO2', name='Formate', compartment='GFOc', charge=-1)
coa_GFOc = Metabolite('coa_GFOc', formula='C21H32N7O16P3S', name='Coenzyme A', compartment='GFOc', charge=-4)
fdox_GFOc = Metabolite('fdox_GFOc', formula='Fe8S8X', name='Ferredoxin-oxidized', compartment='GFOc', charge=0)
fdred_GFOc = Metabolite('fdred_GFOc', formula='Fe8S8X', name='Ferredoxin-reduced', compartment='GFOc', charge=-2)
accoa_GFOc = Metabolite('accoa_GFOc', formula='C23H34N7O17P3S', name='Acetyl-CoA', compartment='GFOc', charge=-4)
co2_GFOc = Metabolite('co2_GFOc', formula='CO2', name='CO2', compartment='GFOc', charge=0)
h_GFOc = Metabolite('h_GFOc', formula='H', name='H+', compartment='GFOc', charge=1)
h_GFOi = Metabolite('h_GFOi', formula='H', name='h_GFOi', compartment='i', charge=1)
h2_GFOc = Metabolite('h2_GFOc', formula='H2', name='Hydrogen', compartment='GFOc', charge=0)
ac_GFOc = Metabolite('ac_GFOc', formula='C2H3O2', name='Acetate', compartment='GFOc', charge=-1)
actp_GFOc = Metabolite('actp_GFOc', formula='C2H3O5P', name='Acetyl Phosphate', compartment='GFOc', charge=-2)
adp_GFOc = Metabolite('adp_GFOc', formula='C10H12N5O10P2', name='ADP C10H12N5O10P2', compartment='GFOc', charge=-3)
atp_GFOc = Metabolite('atp_GFOc', formula='C10H12N5O13P3', name='ATP C10H12N5O13P3', compartment='GFOc', charge=-4)
pi_GFOc = Metabolite('pi_GFOc', formula='HO4P', name='Phosphate', compartment='GFOc', charge=-2)
co_GFOc = Metabolite('co_GFOc', formula='CO', name='Carbon Monoxide', compartment='GFOc', charge=0)
fdxo_42_GFOc = Metabolite('fdxo_42_GFOc', formula='Fe12S12X', name='Ferredoxin - oxidized', compartment='GFOc',charge=0)
fdxr_42_GFOc = Metabolite('fdxr_42_GFOc', formula='Fe12S12X', name='Ferredoxin - reduced', compartment='GFOc',charge=-3)
g6p_GFOc = Metabolite('g6p_GFOc', formula='C6H11O9P', name='Glucose-6-P', compartment='GFOc', charge=-2)
f6p_GFOc = Metabolite('f6p_GFOc', formula='C6H11O9P', name='Fructose-6-P', compartment='GFOc', charge=-2)
fdp_GFOc = Metabolite('fdp_GFOc', formula='C6H10O12P2', name='D-Fructose 1,6-bisphosphate', compartment='GFOc',charge=-4)
dhap_GFOc = Metabolite('dhap_GFOc', formula='C3H5O6P', name='Dihydroxyacetone phosphate', compartment='GFOc', charge=-2)
g3p_GFOc = Metabolite('g3p_GFOc', formula='C3H5O6P', name='Glyceraldehyde 3-phosphate', compartment='GFOc', charge=-2)
nad_GFOc = Metabolite('nad_GFOc', formula='C21H26N7O14P2', name='Nicotinamide adenine dinucleotide', compartment='GFOc',charge=-1)
nadh_GFOc = Metabolite('nadh_GFOc', formula='C21H27N7O14P2', name='Nicotinamide adenine dinucleotide - reduced',compartment='GFOc', charge=-2)
_13dpg_GFOc = Metabolite('_13dpg_GFOc', formula='C3H4O10P2', name='3-Phospho-D-glyceroyl phosphate', compartment='GFOc',charge=-4)
_3pg_GFOc = Metabolite('_3pg_GFOc', formula='C3H4O7P', name='3-Phospho-D-glycerate', compartment='GFOc', charge=-3)
_2pg_GFOc = Metabolite('_2pg_GFOc', formula='C3H4O7P', name='2-Phospho-D-glycerate', compartment='GFOc', charge=-3)
lac__D_GFOc = Metabolite('lac__D_GFOc', formula='C3H5O3', name='D-Lactate', compartment='CELLc', charge=-1)
ppi_GFOc = Metabolite('ppi_GFOc', formula='HO7P2', name='Diphosphate', compartment='GFOc', charge=-3)
e4p_GFOc = Metabolite('e4p_GFOc', formula='C4H7O7P', name='D-Erythrose 4-phosphate', compartment='GFOc', charge=-2)
s7p_GFOc = Metabolite('s7p_GFOc', formula='C7H13O10P', name='Sedoheptulose 7-phosphate', compartment='GFOc', charge=-2)
r5p_GFOc = Metabolite('r5p_GFOc', formula='C5H9O8P', name='Alpha-D-Ribose 5-phosphate', compartment='GFOc', charge=-2)
xu5p__D_GFOc = Metabolite('xu5p__D_GFOc', formula='C5H9O8P', name='D-Xylulose 5-phosphate', compartment='GFOc',charge=-2)
ru5p__D_GFOc = Metabolite('ru5p__D_GFOc', formula='C5H9O8P', name='D-Ribulose 5-phosphate', compartment='GFOc',charge=-2)
_6pgc_GFOc = Metabolite('_6pgc_GFOc', formula='C6H10O10P', name='6-Phospho-D-gluconate', compartment='GFOc', charge=-3)
glc__D_e = Metabolite('glc__D_e', formula='C6H12O6', name='D-Glucose', compartment='e', charge=0)
h2o_e = Metabolite('h2o_e', formula='H2O', name='H2O', compartment='e', charge=0)
pi_e = Metabolite('pi_e', formula='HO4P', name='Phosphate', compartment='e', charge=-2)
ppi_e = Metabolite('ppi_e', formula='HO7P2', name='Diphosphate', compartment='e', charge=-3)
biomass_e = Metabolite('biomass_e', formula='', name='Biomass_e', compartment='e', charge=0)
co2_e = Metabolite('co2_e', formula='CO2', name='CO2', compartment='e', charge=0)
nh4_e = Metabolite('nh4_e', formula='NH4', name='Ammonium', compartment='e', charge=1)
so4_e = Metabolite('so4_e', formula='O4S', name='Sulfate', compartment='e', charge=-2)
for_e = Metabolite('for_e', formula='CHO2', name='Formate', compartment='e', charge=-1)
fum_e = Metabolite('fum_e', formula='C4H2O4', name='Fumarate', compartment='e', charge=-2)
lac__D_e = Metabolite('lac__D_e', formula='C3H5O3', name='D-Lactate', compartment='e', charge=-1)
h_e = Metabolite('h_e', formula='H', name='H+', compartment='e', charge=1)
ac_e = Metabolite('ac_e', formula='C2H3O2', name='Acetate', compartment='e', charge=-1)
h2_e = Metabolite('h2_e', formula='H2', name='Hydrogen', compartment='e', charge=0)

# GLYCOLYSIS

# First Reaction: GLUK
reaction = Reaction('GFO_GLUK')
reaction.name = 'GFO: Glucokinase'
reaction.subsystem = 'Glycolysis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({glc__D_GFOc: -1.0,
                          atp_GFOc: -1.0,
                          g6p__B_GFOc: 1.0,
                          adp_GFOc: 1.0,
                          h_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# G6PI
reaction = Reaction('GFO_G6PI')
reaction.name = 'GFO: Glucose 6 phosphate isomerase - 1'
reaction.subsystem = 'Glycolysis'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g6p_GFOc: -1,
                          g6p__B_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PGI
reaction = Reaction('GFO_PGI')
reaction.name = 'GFO: Glucose 6 phosphate isomerase - 2'
reaction.subsystem = 'Glycolysis'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g6p_GFOc: -1,
                          f6p_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PFK
reaction = Reaction('GFO_PFK')
reaction.name = 'GFO: Phosphofructokinase'
reaction.subsystem = 'Glycolysis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({f6p_GFOc: -1.0,
                          atp_GFOc: -1.0,
                          fdp_GFOc: 1.0,
                          adp_GFOc: 1.0,
                          h_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FBA
reaction = Reaction('GFO_FBA')
reaction.name = 'GFO: Fructose-bisphosphate aldolase'
reaction.subsystem = 'Upper Glycolysis'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({fdp_GFOc: -1.0,
                          dhap_GFOc: 1.0,
                          g3p_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TPI
reaction = Reaction('GFO_TPI')
reaction.name = 'GFO: Triose-phosphate isomerase'
reaction.subsystem = 'Upper Glycolysis'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({dhap_GFOc: -1.0,
                          g3p_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# LOWER GLYCOLYSIS

# GAPD
reaction = Reaction('GFO_GAPD')
reaction.name = 'GFO: Glyceraldehyde-3-phosphate dehydrogenase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g3p_GFOc: -1.0,
                          nad_GFOc: -1.0,
                          pi_GFOc: -1.0,
                          _13dpg_GFOc: 1.0,
                          h_GFOc: 1.0,
                          nadh_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PGK
reaction = Reaction('GFO_PGK')
reaction.name = 'GFO: Phosphoglycerate kinase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({_3pg_GFOc: -1.0,
                          atp_GFOc: -1.0,
                          _13dpg_GFOc: 1.0,
                          adp_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PGM
reaction = Reaction('GFO_PGM')
reaction.name = 'GFO: Phosphoglycerate mutase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({_2pg_GFOc: -1.0,
                          _3pg_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ENO
reaction = Reaction('GFO_ENO')
reaction.name = 'GFO: Enolase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({_2pg_GFOc: -1.0,
                          h2o_GFOc: 1.0,
                          pep_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PYK
reaction = Reaction('GFO_PYK')
reaction.name = 'GFO: Pyruvate kinase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({adp_GFOc: -1.0,
                          h_GFOc: -1.0,
                          pep_GFOc: -1.0,
                          atp_GFOc: 1.0,
                          pyr_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# GLUCONEOGENESIS

# PPS
reaction = Reaction('GFO_PPS')
reaction.name = 'GFO: Phosphoenolpyruvate synthase'
reaction.subsystem = 'Gluconeogenesis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({atp_GFOc: -1.0,
                          h2o_GFOc: -1.0,
                          pyr_GFOc: -1.0,
                          amp_GFOc: 1.0,
                          h_GFOc: 2.0,
                          pep_GFOc: 1.0,
                          pi_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FBP
reaction = Reaction('GFO_FBP')
reaction.name = 'GFO: Fructose-bisphosphatase'
reaction.subsystem = 'Gluconeogenesis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({fdp_GFOc: -1.0,
                          h2o_GFOc: -1.0,
                          f6p_GFOc: 1.0,
                          pi_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TCA CYCLE

# CS
reaction = Reaction('GFO_CS')
reaction.name = 'GFO: Citrate synthase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_GFOc: -1.0,
                          h2o_GFOc: -1.0,
                          oaa_GFOc: -1.0,
                          cit_GFOc: 1.0,
                          coa_GFOc: 1.0,
                          h_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACONT
reaction = Reaction('GFO_ACONT')
reaction.name = 'GFO: Aconitate hydratase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({cit_GFOc: -1.0,
                          icit_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# iCDHx
reaction = Reaction('GFO_GFOiCDHx')
reaction.name = 'GFO: Isocitrate dehydrogenase (NAD)'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({icit_GFOc: -1.0,
                          nad_GFOc: -1.0,
                          akg_GFOc: 1.0,
                          co2_GFOc: 1.0,
                          nadh_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# AKGDH
reaction = Reaction('GFO_AKGDH')
reaction.name = 'GFO: 2-Oxoglutarate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({akg_GFOc: -1.0,
                          coa_GFOc: -1.0,
                          nad_GFOc: -1.0,
                          co2_GFOc: 1.0,
                          nadh_GFOc: 1.0,
                          succoa_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# SUCOAS
reaction = Reaction('GFO_SUCOAS')
reaction.name = 'GFO: Succinyl-CoA synthetase (ADP-forming)'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({adp_GFOc: 1.0,
                          atp_GFOc: -1.0,
                          coa_GFOc: -1.0,
                          pi_GFOc: 1.0,
                          succ_GFOc: -1.0,
                          succoa_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# SUCD1
reaction = Reaction('GFO_SUCD1')
reaction.name = 'GFO: Succinate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({fad_GFOc: -1.0,
                          fadh2_GFOc: 1.0,
                          fum_GFOc: 1.0,
                          succ_GFOc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FUM
reaction = Reaction('GFO_FUM')
reaction.name = 'GFO: Fumarase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({fum_GFOc: -1.0,
                          h2o_GFOc: -1.0,
                          mal__L_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# mDH
reaction = Reaction('GFO_mDH')
reaction.name = 'GFO: Malate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({mal__L_GFOc: -1.0,
                          nad_GFOc: -1.0,
                          oaa_GFOc: 1.0,
                          nadh_GFOc: 1.0,
                          h_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# iCL
reaction = Reaction('GFO_GFOiCL')
reaction.name = 'GFO: Isocitrate lyase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({icit_GFOc: -1.0,
                          glx_GFOc: 1.0,
                          succ_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# mALS
reaction = Reaction('GFO_mALS')
reaction.name = 'GFO: Malate synthase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_GFOc: -1.0,
                          glx_GFOc: -1.0,
                          h2o_GFOc: -1.0,
                          coa_GFOc: 1.0,
                          h_GFOc: 1.0,
                          mal__L_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ATP SYNTHASE 4
reaction = Reaction('GFO_ATPS4')
reaction.name = 'GFO: ATP Synthase'
reaction.subsystem = 'Electron Transport Chain'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({adp_GFOc: -1.0,
                          pi_GFOc: -1.0,
                          h_GFOc: 3.0,
                          h2o_GFOc: 1.0,
                          h_GFOi: -4.0,
                          atp_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ATP HYDROLYSIS
reaction = Reaction('GFO_ATPHydr')
reaction.name = 'GFO: ATP Hydrolysis'
reaction.subsystem = 'ATP Demand'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({atp_GFOc: -1.0,
                          pi_GFOc: 1.0,
                          h_GFOc: 1.0,
                          h2o_GFOc: -1.0,
                          adp_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PENTOSE PHOSPHATE PATHWAY

# G6PDH2r
reaction = Reaction('GFO_G6PDH2r')
reaction.name = 'GFO: Glucose 6-phosphate dehydrogenase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g6p_GFOc: -1.0,
                          nadp_GFOc: -1.0,
                          _6pgl_GFOc: 1.0,
                          h_GFOc: 1.0,
                          nadph_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PGL
reaction = Reaction('GFO_PGL')
reaction.name = 'GFO: 6-phosphogluconolactonase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({_6pgl_GFOc: -1.0,
                          h2o_GFOc: -1.0,
                          _6pgc_GFOc: 1.0,
                          h_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# GND
reaction = Reaction('GFO_GND')
reaction.name = 'GFO: Phosphogluconate dehydrogenase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({_6pgc_GFOc: -1.0,
                          nadp_GFOc: -1.0,
                          ru5p__D_GFOc: 1.0,
                          co2_GFOc: 1.0,
                          nadph_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# RPE
reaction = Reaction('GFO_RPE')
reaction.name = 'GFO: Ribulose 5-phosphate 3-epimerase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({ru5p__D_GFOc: -1.0,
                          xu5p__D_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# RPI
reaction = Reaction('GFO_RPI')
reaction.name = 'GFO: Ribose-5-phosphate isomerase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({r5p_GFOc: 1.0,
                          xu5p__D_GFOc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TKT1
reaction = Reaction('GFO_TKT1')
reaction.name = 'GFO: Transketolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({r5p_GFOc: -1.0,
                          xu5p__D_GFOc: -1.0,
                          g3p_GFOc: 1.0,
                          s7p_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TALA
reaction = Reaction('GFO_TALA')
reaction.name = 'GFO: Transaldolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g3p_GFOc: -1.0,
                          s7p_GFOc: -1.0,
                          e4p_GFOc: 1.0,
                          f6p_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TKT2
reaction = Reaction('GFO_TKT2')
reaction.name = 'GFO: Transketolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({e4p_GFOc: -1.0,
                          xu5p__D_GFOc: -1.0,
                          g3p_GFOc: 1.0,
                          f6p_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# NADPH - NADH CONVERSION

# THD
reaction = Reaction('GFO_THD')
reaction.name = 'GFO: NADPH Transhydorgenase'
reaction.subsystem = 'NADPH - NADH Conversion'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({nadh_GFOc: -1.0,
                          nadp_GFOc: -1.0,
                          h_GFOi: -1.0,
                          h_GFOc: 1.0,
                          nadph_GFOc: 1.0,
                          nad_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACETATE METABOLISM

# PTAr
reaction = Reaction('GFO_PTAr')
reaction.name = 'GFO: Acetate metabolism'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_GFOc: -1.0,
                          pi_GFOc: -1.0,
                          actp_GFOc: 1.0,
                          coa_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACKr
reaction = Reaction('GFO_ACKr')
reaction.name = 'GFO: Acetate kinase'
reaction.subsystem = 'Acetate metabolism'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({ac_GFOc: 1.0,
                          atp_GFOc: 1.0,
                          actp_GFOc: -1.0,
                          adp_GFOc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# DIPHOSPHATE HYDROLYSIS

# PPA
reaction = Reaction('GFO_PPA')
reaction.name = 'GFO: Inorganic diphosphatase'
reaction.subsystem = 'Diphosphate hydrolysis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h2o_GFOc: -1.0,
                          ppi_GFOc: -1.0,
                          h_GFOc: 1.0,
                          pi_GFOc: 2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# AMP RECYCLING

# ADK1
reaction = Reaction('GFO_ADK1')
reaction.name = 'GFO: Adenylate kinase'
reaction.subsystem = 'AMP Recycling'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({amp_GFOc: -1.0,
                          atp_GFOc: -1.0,
                          adp_GFOc: 2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# LACTATE METABOLISM

# LDH-D
reaction = Reaction('GFO_LDH-D')
reaction.name = 'GFO: D-lactate dehydrogenase'
reaction.subsystem = 'Lactate metabolism'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({lac__D_GFOc: -1.0,
                          nad_GFOc: -1.0,
                          h_GFOc: 1.0,
                          nadh_GFOc: 1.0,
                          pyr_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# GIVEN GFO RXNS

# PFOR-F
reaction = Reaction('PFOR-F')
reaction.name = 'Pyruvate Ferredoxin Oxidoreductase'
reaction.subsystem = 'Glucose Fermenters'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({pyr_GFOc: -1.0,
                          fdox_GFOc: -1.0,
                          coa_GFOc: -1.0,
                          fdred_GFOc: 1.0,
                          co2_GFOc: 1.0,
                          accoa_GFOc: 1.0,
                          h_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# HYD1
reaction = Reaction('HYDR1')
reaction.name = 'Ferredoxin Hydrogenase'
reaction.subsystem = 'Glucose Fermenters'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({fdred_GFOc: -1.0,
                          h_GFOc: -2.0,
                          fdox_GFOc: 1.0,
                          h2_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ECH
reaction = Reaction('GFO_ECH')
reaction.name = 'Energy-Conserving Hydrogenase'
reaction.subsystem = 'Glucose Fermenters'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({fdred_GFOc: -1.0,
                          h_GFOc: -3.0,
                          h_GFOi: 1.0,
                          h2_GFOc: 1.0,
                          fdox_GFOc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# RNF Complex
reaction = Reaction('GFO_RNF')
reaction.name = 'GFO: RNF'
reaction.subsystem = 'Energy conservation'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({fdred_GFOc: -1.0,
                          nad_GFOc: -1.0,
                          h_GFOc: -3.0,
                          fdox_GFOc: 1.0,
                          nadh_GFOc: 1.0,
                          h_GFOi: 2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# BIOMASS RXN
# ADD COUNTING METABOLITE FOR COMMUNITY BIOMASS
biomass_COMMUNITY = Metabolite('biomass_COMMUNITY', formula='', name='Biomass', compartment='e', charge=0)

# BIOMASS
reaction = Reaction('GFO_BIOMASS')
reaction.name = 'GFO: Biomass'
reaction.subsystem = 'Biomass'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({akg_GFOc: -1.17,
                          oaa_GFOc: -2.06,
                          g6p_GFOc: -0.26,
                          g3p_GFOc: -1.58,
                          _3pg_GFOc: -1.31,
                          pyr_GFOc: -4.33,
                          pep_GFOc: -0.92,
                          accoa_GFOc: -3.06,
                          e4p_GFOc: -0.40,
                          r5p_GFOc: -0.35,
                          fum_GFOc: 0.37,
                          ac_GFOc: 0.43,
                          for_GFOc: 0.29,
                          atp_GFOc: -36.0,
                          nadph_GFOc: -19.39,
                          nadh_GFOc: 1.10,
                          nh4_GFOc: -8.62,
                          h_GFOc: 10.13,
                          adp_GFOc: 34.6,
                          pi_GFOc: 31.88,
                          ppi_GFOc: 4.74,
                          amp_GFOc: 1.4,
                          co2_GFOc: 3.54,
                          h2o_GFOc: -7.57,
                          coa_GFOc: 3.06,
                          nad_GFOc: -1.10,
                          nadp_GFOc: 19.39,
                          so4_GFOc: -0.21,
                          biomass_GFOc: 1.0,
                          biomass_COMMUNITY: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# GFO - TRANSPORT RXNS
reaction = Reaction('GFO_Transport_H2')
reaction.name = 'GFO: Transport - H2'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h2_GFOc: 1.0,
                          h2_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_Acetate')
reaction.name = 'GFO: Transport - Acetate'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({ac_GFOc: 1.0,
                          ac_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_h2o')
reaction.name = 'GFO: Transport - h2o'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h2o_GFOc: 1.0,
                          h2o_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_pi')
reaction.name = 'GFO: Transport - po4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({pi_GFOc: 1.0,
                          pi_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_ppi')
reaction.name = 'GFO: Transport - po4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({ppi_GFOc: 1.0,
                          ppi_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_biomass')
reaction.name = 'GFO: Transport - biomass'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({biomass_GFOc: 1.0,
                          biomass_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_co2')
reaction.name = 'GFO: Transport - co2'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({co2_GFOc: 1.0,
                          co2_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_nh4')
reaction.name = 'GFO: Transport - nh4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({nh4_GFOc: 1.0,
                          nh4_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_so4')
reaction.name = 'GFO: Transport - so4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({so4_GFOc: 1.0,
                          so4_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_for')
reaction.name = 'GFO: Transport - for'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({for_GFOc: 1.0,
                          for_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_fum')
reaction.name = 'GFO: Transport - fum'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({fum_GFOc: 1.0,
                          fum_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_lac')
reaction.name = 'GFO: Transport - lac'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({lac__D_GFOc: 1.0,
                          lac__D_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_h')
reaction.name = 'GFO: Transport - h'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h_GFOc: 1.0,
                          h_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('GFO_Transport_Glucose')
reaction.name = 'GFO: Transport - Glucose'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({glc__D_GFOc: 1.0,
                          glc__D_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# EXCHANGE RXNS

# GLUCOSE EXCHANGE
reaction = Reaction('EX_glc__D')
reaction.name = 'Exchange - Glucose'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({glc__D_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# H2O EXCHANGE
reaction = Reaction('EX_h2o')
reaction.name = 'Exchange - h2o'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h2o_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PI EXCHANGE
reaction = Reaction('EX_pi')
reaction.name = 'Exchange - pi'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({pi_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PPI EXCHANGE
reaction = Reaction('EX_ppi')
reaction.name = 'Exchange - ppi'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({ppi_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# BIOMASS EXCHANGE
reaction = Reaction('EX_biomass')
reaction.name = 'Exchange - biomass'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({biomass_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# CO2 EXCHANGE
reaction = Reaction('EX_co2')
reaction.name = 'Exchange - co2'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({co2_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# NH4 EXCHANGE
reaction = Reaction('EX_nh4')
reaction.name = 'Exchange - nh4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({nh4_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# SO4 EXCHANGE
reaction = Reaction('EX_so4')
reaction.name = 'Exchange - so4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({so4_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FOR EXCHANGE
reaction = Reaction('EX_for')
reaction.name = 'Exchange - for'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({for_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FUM EXCHANGE
reaction = Reaction('EX_fum')
reaction.name = 'Exchange - fum'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({fum_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# H2 EXCHANGE
reaction = Reaction('EX_H2')
reaction.name = 'Exchange - H2'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({h2_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# LAC EXCHANGE
reaction = Reaction('EX_lac')
reaction.name = 'Exchange - lac'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({lac__D_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# H EXCHANGE
reaction = Reaction('EX_h')
reaction.name = 'Exchange - h'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACETATE EXCHANGE
reaction = Reaction('EX_ac')
reaction.name = 'Exchange - Acetate'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({ac_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# DEMAND FOR COMMUNITY BIOMASS
reaction = Reaction('DEMAND_biomass_COMMUNITY')
reaction.name = 'Demand - biomass_COMMUNITY '
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({biomass_COMMUNITY: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

print(f'{len(model.reactions)} reactions')
print(f'{len(model.metabolites)} metabolites')

######################################################################################################################
########################################################################################################################
########################################################################################################################

# HMAs !!!!!!!
pyr_HMAc = Metabolite('pyr_HMAc', formula='C3H3O3', name='Pyruvate', compartment='HMAc', charge=-1)
amp_HMAc = Metabolite('amp_HMAc', formula='C10H12N5O7P', name='AMP', compartment='HMAc', charge=-2)
cit_HMAc = Metabolite('cit_HMAc', formula='C6H5O7', name='Citrate', compartment='HMAc', charge=-3)
oaa_HMAc = Metabolite('oaa_HMAc', formula='C4H2O5', name='Oxaloacetate', compartment='HMAc', charge=-2)
_6pgl_HMAc = Metabolite('_6pgl_HMAc', formula='C6H9O9P', name='6-phospho-D-glucono-1,5-lactone', compartment='HMAc',charge=-2)
nadp_HMAc = Metabolite('nadp_HMAc', formula='C21H25N7O17P3', name='Nicotinamide adenine dinucleotide phosphate',compartment='HMAc', charge=-3)
nadph_HMAc = Metabolite('nadph_HMAc', formula='C21H26N7O17P3',name='Nicotinamide adenine dinucleotide phosphate - reduced', compartment='HMAc', charge=-4)
glx_HMAc = Metabolite('glx_HMAc', formula='C2HO3', name='Glyoxylate', compartment='CELLc', charge=-1)
fum_HMAc = Metabolite('fum_HMAc', formula='C4H2O4', name='Fumarate', compartment='HMAc', charge=-2)
mal__L_HMAc = Metabolite('mal__L_HMAc', formula='C4H4O5', name='L-Malate', compartment='HMAc', charge=-2)
fad_HMAc = Metabolite('fad_HMAc', formula='C27H31N9O15P2', name='Flavin adenine dinucleotide oxidized', compartment='HMAc', charge=-2)
fadh2_HMAc = Metabolite('fadh2_HMAc', formula='C27H33N9O15P2', name='Flavin adenine dinucleotide reduced',compartment='HMAc', charge=-2)
succ_HMAc = Metabolite('succ_HMAc', formula='C4H4O4', name='Succinate', compartment='HMAc', charge=-2)
succoa_HMAc = Metabolite('succoa_HMAc', formula='C25H35N7O19P3S', name='Succinyl-CoA', compartment='HMAc', charge=-5)
akg_HMAc = Metabolite('akg_HMAc', formula='C5H4O5', name='2-Oxoglutarate', compartment='HMAc', charge=-2)
icit_HMAc = Metabolite('icit_HMAc', formula='C6H5O7', name='Isocitrate', compartment='HMAc', charge=-3)
pep_HMAc = Metabolite('pep_HMAc', formula='C3H2O6P', name='Phosphoenolpyruvate', compartment='HMAc', charge=-3)
h2o_HMAc = Metabolite('h2o_HMAc', formula='H2O', name='H2O', compartment='HMAc', charge=0)
glc__D_HMAc = Metabolite('glc__D_HMAc', formula='C6H12O6', name='D-Glucose', compartment='HMAc', charge=0)
g6p__B_HMAc = Metabolite('g6p__B_HMAc', formula='C6H11O9P', name='B-Glucose-6-P', compartment='HMAc', charge=-2)
biomass_HMAc = Metabolite('biomass_HMAc', formula='', name='Biomass', compartment='HMAc', charge=0)
nh4_HMAc = Metabolite('nh4_HMAc', formula='NH4', name='Ammonium', compartment='HMAc', charge=1)
so4_HMAc = Metabolite('so4_HMAc', formula='O4S', name='Sulfate', compartment='HMAc', charge=-2)
for_HMAc = Metabolite('for_HMAc', formula='CHO2', name='Formate', compartment='HMAc', charge=-1)
coa_HMAc = Metabolite('coa_HMAc', formula='C21H32N7O16P3S', name='Coenzyme A', compartment='HMAc', charge=-4)
fdox_HMAc = Metabolite('fdox_HMAc', formula='Fe8S8X', name='Ferredoxin-oxidized', compartment='HMAc', charge=0)
fdred_HMAc = Metabolite('fdred_HMAc', formula='Fe8S8X', name='Ferredoxin-reduced', compartment='HMAc', charge=-2)
accoa_HMAc = Metabolite('accoa_HMAc', formula='C23H34N7O17P3S', name='Acetyl-CoA', compartment='HMAc', charge=-4)
co2_HMAc = Metabolite('co2_HMAc', formula='CO2', name='CO2', compartment='HMAc', charge=0)
h_HMAc = Metabolite('h_HMAc', formula='H', name='H+', compartment='HMAc', charge=1)
h_HMAi = Metabolite('h_HMAi', formula='H', name='h_HMAi', compartment='i', charge=1)
h2_HMAc = Metabolite('h2_HMAc', formula='H2', name='Hydrogen', compartment='HMAc', charge=0)
ac_HMAc = Metabolite('ac_HMAc', formula='C2H3O2', name='Acetate', compartment='HMAc', charge=-1)
actp_HMAc = Metabolite('actp_HMAc', formula='C2H3O5P', name='Acetyl Phosphate', compartment='HMAc', charge=-2)
adp_HMAc = Metabolite('adp_HMAc', formula='C10H12N5O10P2', name='ADP C10H12N5O10P2', compartment='HMAc', charge=-3)
atp_HMAc = Metabolite('atp_HMAc', formula='C10H12N5O13P3', name='ATP C10H12N5O13P3', compartment='HMAc', charge=-4)
pi_HMAc = Metabolite('pi_HMAc', formula='HO4P', name='Phosphate', compartment='HMAc', charge=-2)
co_HMAc = Metabolite('co_HMAc', formula='CO', name='Carbon Monoxide', compartment='HMAc', charge=0)
fdxo_42_HMAc = Metabolite('fdxo_42_HMAc', formula='Fe12S12X', name='Ferredoxin - oxidized', compartment='HMAc',charge=0)
fdxr_42_HMAc = Metabolite('fdxr_42_HMAc', formula='Fe12S12X', name='Ferredoxin - reduced', compartment='HMAc',charge=-3)
g6p_HMAc = Metabolite('g6p_HMAc', formula='C6H11O9P', name='Glucose-6-P', compartment='HMAc', charge=-2)
f6p_HMAc = Metabolite('f6p_HMAc', formula='C6H11O9P', name='Fructose-6-P', compartment='HMAc', charge=-2)
fdp_HMAc = Metabolite('fdp_HMAc', formula='C6H10O12P2', name='D-Fructose 1,6-bisphosphate', compartment='HMAc',charge=-4)
dhap_HMAc = Metabolite('dhap_HMAc', formula='C3H5O6P', name='Dihydroxyacetone phosphate', compartment='HMAc', charge=-2)
g3p_HMAc = Metabolite('g3p_HMAc', formula='C3H5O6P', name='Glyceraldehyde 3-phosphate', compartment='HMAc', charge=-2)
nad_HMAc = Metabolite('nad_HMAc', formula='C21H26N7O14P2', name='Nicotinamide adenine dinucleotide', compartment='HMAc',charge=-1)
nadh_HMAc = Metabolite('nadh_HMAc', formula='C21H27N7O14P2', name='Nicotinamide adenine dinucleotide - reduced',compartment='HMAc', charge=-2)
_13dpg_HMAc = Metabolite('_13dpg_HMAc', formula='C3H4O10P2', name='3-Phospho-D-glyceroyl phosphate', compartment='HMAc',charge=-4)
_3pg_HMAc = Metabolite('_3pg_HMAc', formula='C3H4O7P', name='3-Phospho-D-glycerate', compartment='HMAc', charge=-3)
_2pg_HMAc = Metabolite('_2pg_HMAc', formula='C3H4O7P', name='2-Phospho-D-glycerate', compartment='HMAc', charge=-3)
lac__D_HMAc = Metabolite('lac__D_HMAc', formula='C3H5O3', name='D-Lactate', compartment='CELLc', charge=-1)
ppi_HMAc = Metabolite('ppi_HMAc', formula='HO7P2', name='Diphosphate', compartment='HMAc', charge=-3)
e4p_HMAc = Metabolite('e4p_HMAc', formula='C4H7O7P', name='D-Erythrose 4-phosphate', compartment='HMAc', charge=-2)
s7p_HMAc = Metabolite('s7p_HMAc', formula='C7H13O10P', name='Sedoheptulose 7-phosphate', compartment='HMAc', charge=-2)
r5p_HMAc = Metabolite('r5p_HMAc', formula='C5H9O8P', name='Alpha-D-Ribose 5-phosphate', compartment='HMAc', charge=-2)
xu5p__D_HMAc = Metabolite('xu5p__D_HMAc', formula='C5H9O8P', name='D-Xylulose 5-phosphate', compartment='HMAc', charge=-2)
ru5p__D_HMAc = Metabolite('ru5p__D_HMAc', formula='C5H9O8P', name='D-Ribulose 5-phosphate', compartment='HMAc',charge=-2)
_6pgc_HMAc = Metabolite('_6pgc_HMAc', formula='C6H10O10P', name='6-Phospho-D-gluconate', compartment='HMAc', charge=-3)
glc__D_e = Metabolite('glc__D_e', formula='C6H12O6', name='D-Glucose', compartment='e', charge=0)
h2o_e = Metabolite('h2o_e', formula='H2O', name='H2O', compartment='e', charge=0)
pi_e = Metabolite('pi_e', formula='HO4P', name='Phosphate', compartment='e', charge=-2)
ppi_e = Metabolite('ppi_e', formula='HO7P2', name='Diphosphate', compartment='e', charge=-3)
biomass_e = Metabolite('biomass_e', formula='', name='Biomass_e', compartment='e', charge=0)
co2_e = Metabolite('co2_e', formula='CO2', name='CO2', compartment='e', charge=0)
nh4_e = Metabolite('nh4_e', formula='NH4', name='Ammonium', compartment='e', charge=1)
so4_e = Metabolite('so4_e', formula='O4S', name='Sulfate', compartment='e', charge=-2)
for_e = Metabolite('for_e', formula='CHO2', name='Formate', compartment='e', charge=-1)
fum_e = Metabolite('fum_e', formula='C4H2O4', name='Fumarate', compartment='e', charge=-2)
lac__D_e = Metabolite('lac__D_e', formula='C3H5O3', name='D-Lactate', compartment='e', charge=-1)
h_e = Metabolite('h_e', formula='H', name='H+', compartment='e', charge=1)
ac_e = Metabolite('ac_e', formula='C2H3O2', name='Acetate', compartment='e', charge=-1)
mfr_b_HMAc = Metabolite('mfr_b_HMAc', formula='C34H44N6O14', name='A Methanofuran', compartment='HMAc', charge=0)
formmfr_b_HMAc = Metabolite('formmfr_b_HMAc', formula='C35H43N4O15R', name='A Formylmethanofuran', compartment='HMAc',charge=0)
formh4spt_HMAc = Metabolite('formh4spt_HMAc', formula='C36H48N7O20P1', name='Formyltetrahydrosarcinapterin', compartment='HMAc', charge=0)
h4spt_HMAc = Metabolite('h4spt_HMAc', formula='C35H48N7O19P1', name='Tetrahydrosarcinapterin', compartment='HMAc',charge=0)
menylh4spt_HMAc = Metabolite('menylh4spt_HMAc', formula='C36H47N7O19P1', name='Methenyl-tetrahydrosarcinapterin',compartment='HMAc', charge=0)
f420_2_HMAc = Metabolite('f420_2_HMAc', name='Coenzyme ferredoxin 420-2 (oxidized)', formula='C29H34N5O18P',compartment='HMAc', charge=0)
f420_2h2_HMAc = Metabolite('f420_2h2_HMAc', name='Coenzyme ferredoxin 420-2 (reduced)', formula='C29H36O18N5P1',compartment='HMAc', charge=0)
mleneh4spt_HMAc = Metabolite('mleneh4spt_HMAc', name='N5,N10-methylee-5,6,7,8-tetrahydromethanopterin', formula='C36H48N7O19P1', compartment='HMAc', charge=0)
com_HMAc = Metabolite('com_HMAc', name='Coenzyme m', formula='C2H5O3S2', compartment='HMAc', charge=0)
mcom_HMAc = Metabolite('mcom_HMAc', name='Methylcoenzyme m', formula='C3O3S2H7', compartment='HMAc', charge=0)
mphen_HMAc = Metabolite('mphen_HMAc', name='Methanophenazine (oxidized)', formula='C37N2O1H50', compartment='HMAc',charge=0)
mphenh2_HMAc = Metabolite('mphenh2_HMAc', name='Methanophenazine (reduced)', formula='C37N2O1H52', compartment='HMAc',charge=0)
h2_e = Metabolite('h2_e', name='Hydrogen', formula='H2', compartment='e', charge=0)
mh4spt_HMAc = Metabolite('mh4spt_HMA', name='N5-methyl-tetrahydrosarcinapterin', formula='C36H50N7O19P1',compartment='HMAc', charge=0)
ch4_e = Metabolite('ch4_e', formula='CH4', name='Methane', compartment='e', charge=0)
ch4_HMAc = Metabolite('ch4_HMAc', formula='CH4', name='Methane', compartment='HMAc', charge=0)
cob_HMAc = Metabolite('cob_HMAc', formula='C11H19N1O7P1S1', name='Conenzyme B', compartment='HMAc', charge=0)
hsfd_HMAc = Metabolite('hsfd_HMAc', formula='C13H22N1O10P1S3', name='Heterodisulfide', compartment='HMAc', charge=0)

# HMA RXN's from Fig 3

# [1] Formylmethanofuran Dehydrogenase - FMFD_b
reaction = Reaction('HMA_FMFD_b')  # What do we do with R's if they're not balancing?
reaction.name = 'HMA: Formylmethanofuran Dehydrogenase'
reaction.subsystem = 'HMA'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({co2_HMAc: -1.0,
                          fdred_HMAc: -2.0,
                          h_HMAc: -2.0,
                          mfr_b_HMAc: -1.0,
                          fdox_HMAc: 2.0,
                          h2o_HMAc: 1.0,
                          formmfr_b_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# [2] Formylmethanofuran-tetrahydromethanopterin N-formyltransferase - FMFTSPFT_b
reaction = Reaction('HMA_FMFTSPFT_b')
reaction.name = 'HMA: Formylmethanofuran-Tetrahydromethanopterin N-Formyltransferase'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_HMAc: -1.0,
                          h4spt_HMAc: -1.0,
                          mfr_b_HMAc: 1.0,
                          formmfr_b_HMAc: -1.0,
                          formh4spt_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# [3]? MTSPC
reaction = Reaction('HMA_MTSPC')
reaction.name = 'HMA: MTSPC'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_HMAc: -1.0,
                          h2o_HMAc: 1.0,
                          menylh4spt_HMAc: 1.0,
                          formh4spt_HMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# F4RHi [9]
reaction = Reaction('HMA_F4RHi')
reaction.name = 'HMA: Coenzyme F420 Hydrogenase'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h2_HMAc: -1.0,
                          f420_2_HMAc: -1.0,
                          f420_2h2_HMAc: 1.0,
                          h_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# F4MTSPD [4]
reaction = Reaction('HMA_F4MTSPD')
reaction.name = 'HMA: F4MTSPD'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_HMAc: 1.0,
                          f420_2_HMAc: 1.0,
                          f420_2h2_HMAc: -1.0,
                          mleneh4spt_HMAc: 1.0,
                          menylh4spt_HMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# F4MTSPR [5]
reaction = Reaction('HMA_F4MTSPR')
reaction.name = 'HMA: F4MTSPR'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({f420_2_HMAc: 1.0,
                          mh4spt_HMAc: 1.0,
                          f420_2h2_HMAc: -1.0,
                          mleneh4spt_HMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# MTSPCMMT [6]
reaction = Reaction('HMA_MTSPCMMT')
reaction.name = 'HMA: MTSPCMMT'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_HMAc: -1.7,
                          h_HMAi: 1.7,
                          h4spt_HMAc: 1.0,
                          mh4spt_HMAc: -1.0,
                          com_HMAc: -1.0,
                          mcom_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ION MOTIVE FORCE

# F4D (not shown in Fig 3???)
reaction = Reaction('HMA_F4D')
reaction.name = 'HMA: F4D'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_HMAc: -1.8,
                          f420_2h2_HMAc: -1.0,
                          mphen_HMAc: -1.0,
                          h_HMAi: 1.8,
                          f420_2_HMAc: 1.0,
                          mphenh2_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# F4NH (not shown in Fig 3??)
reaction = Reaction('HMA_F4NH')
reaction.name = 'HMA: F4NH'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_HMAc: -1.8,
                          h_HMAi: 1.8,
                          h2_HMAc: -1.0,
                          mphen_HMAc: -1.0,
                          mphenh2_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# MCR
reaction = Reaction('HMA_MCR')
reaction.name = 'HMA: MCR'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({ch4_HMAc: 1.0,
                          cob_HMAc: -1.0,
                          mcom_HMAc: -1.0,
                          hsfd_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# HDR
reaction = Reaction('HMA_HDR')
reaction.name = 'HMA: HDR'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_HMAc: -1.8,
                          h_HMAi: 1.8,
                          cob_HMAc: 1.0,
                          com_HMAc: 1.0,
                          mphen_HMAc: 1.0,
                          mphenh2_HMAc: -1.0,
                          hsfd_HMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ECHH_10
reaction = Reaction('HMA_ECHH_10')
reaction.name = 'HMA: ECHH 10'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_HMAc: -3.0,
                          h2_HMAc: 1.0,
                          h_HMAi: 1.0,
                          fdox_HMAc: 2.0,
                          fdred_HMAc: -2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))


# I got rid of Glycolysis, Upper Glycolysis, and Lower Glycolysis
# DO I NEED GLUCONEOGENESIS RXN PPS?? WHERE IS THE PYRUVATE COMING FROM??
# I KEPT ATP SYNTHASE, BUT DO I NEED TO KEEP ATP HYDROLYSIS?
# should i keep: DIPHOSPHATE HYDROLYSIS, ACETATE METABOLISM, NADPH - NADH CONVERSION
# should i keep: RNF complex, AMP RECYCLING, LACTATE METABOLISM
# I don't have the electron transport chain anywhere, that's ok right
# I never produce lactate in gfo's, right? can i just delete lactate metabolism

# GLUCONEOGENESIS

##AMY- I ADDED A BUNCH OF REACTIONS BELOW FOR GLUCONEOGENESIS
##THESE ARE THE REVERSIBLE GLYCOLYSIS REACTIONS AND ALLOW
##FOR BIOMASS PRECURSORS TO BE PRODUCED

g6p_HMAc = Metabolite('g6p_HMAc', formula='C6H11O9P', name='Glucose-6-P', compartment='HMAc', charge=-2)

reaction = Reaction('HMA_G6PI')
reaction.name = 'HMA: Glucose 6 phosphate isomerase - 1'
reaction.subsystem = 'Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({g6p_HMAc: -1,
                          g6p__B_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Glucose 6 phosphate isomerase - 2
# g6p_HMAc <-> f6p_HMAc
f6p_HMAc = Metabolite('f6p_HMAc', formula='C6H11O9P', name='Fructose-6-P', compartment='HMAc', charge=-2)

reaction = Reaction('HMA_PGI')
reaction.name = 'HMA: Glucose 6 phosphate isomerase - 2'
reaction.subsystem = 'Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({g6p_HMAc: -1,
                          f6p_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))


# Fructose-bisphosphate aldolase
# fdp_HMAc <-> dhapLc + g3p_HMAc
dhap_HMAc = Metabolite('dhap_HMAc', formula='C3H5O6P', name='Dihydroxyacetone phosphate', compartment='HMAc', charge=-2)
g3p_HMAc = Metabolite('g3p_HMAc', formula='C3H5O6P', name='Glyceraldehyde 3-phosphate', compartment='HMAc', charge=-2)

reaction = Reaction('HMA_FBA')
reaction.name = 'HMA: Fructose-bisphosphate aldolase'
reaction.subsystem = 'Upper Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({fdp_HMAc: -1.0,
                          dhap_HMAc: 1.0,
                          g3p_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Triose-phosphate isomerase
# dhap_HMAc <-> g3p_HMAc

reaction = Reaction('HMA_TPI')
reaction.name = 'HMA: Triose-phosphate isomerase'
reaction.subsystem = 'Upper Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({dhap_HMAc: -1.0,
                          g3p_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# LOWER GLYCOLYSIS

# Glyceraldehyde-3-phosphate dehydrogenase
# g3p_HMAc + nad_HMAc + pi_HMAc <-> 13dpg_HMAc + h_HMAc + nadh_HMAc
nad_HMAc = Metabolite('nad_HMAc', formula='C21H26N7O14P2', name='Nicotinamide adenine dinucleotide', compartment='HMAc',
                      charge=-1)
nadh_HMAc = Metabolite('nadh_HMAc', formula='C21H27N7O14P2', name='Nicotinamide adenine dinucleotide - reduced',
                       compartment='HMAc', charge=-2)
_13dpg_HMAc = Metabolite('_13dpg_HMAc', formula='C3H4O10P2', name='3-Phospho-D-glyceroyl phosphate', compartment='HMAc',
                         charge=-4)
pi_HMAc = Metabolite('pi_HMAc', formula='HO4P', name='Phosphate', compartment='HMAc', charge=-2)

reaction = Reaction('HMA_GAPD')
reaction.name = 'HMA: Glyceraldehyde-3-phosphate dehydrogenase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({g3p_HMAc: -1.0,
                          nad_HMAc: -1.0,
                          pi_HMAc: -1.0,
                          _13dpg_HMAc: 1.0,
                          h_HMAc: 1.0,
                          nadh_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Phosphoglycerate kinase
# 3pg_HMAc + atp_HMAc <-> 13dpg_HMAc + adp_HMAc
_3pg_HMAc = Metabolite('_3pg_HMAc', formula='C3H4O7P', name='3-Phospho-D-glycerate', compartment='HMAc', charge=-3)

reaction = Reaction('HMA_PGK')
reaction.name = 'HMA: Phosphoglycerate kinase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({_3pg_HMAc: -1.0,
                          atp_HMAc: -1.0,
                          _13dpg_HMAc: 1.0,
                          adp_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Phosphoglycerate mutase
# 2pg_HMAc <-> 3pg_HMAc
_2pg_HMAc = Metabolite('_2pg_HMAc', formula='C3H4O7P', name='2-Phospho-D-glycerate', compartment='HMAc', charge=-3)

reaction = Reaction('HMA_PGM')
reaction.name = 'HMA: Phosphoglycerate mutase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({_2pg_HMAc: -1.0,
                          _3pg_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Enolase
# 2pg_HMAc <-> h2o_HMAc + pep_HMAc
pep_HMAc = Metabolite('pep_HMAc', formula='C3H2O6P', name='Phosphoenolpyruvate', compartment='HMAc', charge=-3)
h2o_HMAc = Metabolite('h2o_HMAc', formula='H2O', name='H2O', compartment='HMAc', charge=0)

reaction = Reaction('HMA_ENO')
reaction.name = 'HMA: Enolase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({_2pg_HMAc: -1.0,
                          h2o_HMAc: 1.0,
                          pep_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Pyruvate kinase
# adp_HMAc + h_HMAc + pep_HMAc <-> atp_HMAc + pyr_HMAc
pyr_HMAc = Metabolite('pyr_HMAc', formula='C3H3O3', name='Pyruvate', compartment='HMAc', charge=-1)

reaction = Reaction('HMA_PYK')
reaction.name = 'HMA: Pyruvate kinase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = 0.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({adp_HMAc: -1.0,
                          h_HMAc: -1.0,
                          pep_HMAc: -1.0,
                          atp_HMAc: 1.0,
                          pyr_HMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PPS
reaction = Reaction('HMA_PPS')
reaction.name = 'HMA: Phosphoenolpyruvate synthase'
reaction.subsystem = 'Gluconeogenesis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({atp_HMAc: -1.0,
                          h2o_HMAc: -1.0,
                          pyr_HMAc: -1.0,
                          amp_HMAc: 1.0,
                          h_HMAc: 2.0,
                          pep_HMAc: 1.0,
                          pi_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FBP
reaction = Reaction('HMA_FBP')
reaction.name = 'HMA: Fructose-bisphosphatase'
reaction.subsystem = 'Gluconeogenesis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({fdp_HMAc: -1.0,
                          h2o_HMAc: -1.0,
                          f6p_HMAc: 1.0,
                          pi_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TCA CYCLE

# CS
reaction = Reaction('HMA_CS')
reaction.name = 'HMA: Citrate synthase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_HMAc: -1.0,
                          h2o_HMAc: -1.0,
                          oaa_HMAc: -1.0,
                          cit_HMAc: 1.0,
                          coa_HMAc: 1.0,
                          h_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACONT
reaction = Reaction('HMA_ACONT')
reaction.name = 'HMA: Aconitate hydratase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({cit_HMAc: -1.0,
                          icit_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# iCDHx
reaction = Reaction('HMA_HMAiCDHx')
reaction.name = 'HMA: Isocitrate dehydrogenase (NAD)'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({icit_HMAc: -1.0,
                          nad_HMAc: -1.0,
                          akg_HMAc: 1.0,
                          co2_HMAc: 1.0,
                          nadh_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# AKGDH
reaction = Reaction('HMA_AKGDH')
reaction.name = 'HMA: 2-Oxoglutarate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({akg_HMAc: -1.0,
                          coa_HMAc: -1.0,
                          nad_HMAc: -1.0,
                          co2_HMAc: 1.0,
                          nadh_HMAc: 1.0,
                          succoa_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# SUCOAS
reaction = Reaction('HMA_SUCOAS')
reaction.name = 'HMA: Succinyl-CoA synthetase (ADP-forming)'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({adp_HMAc: 1.0,
                          atp_HMAc: -1.0,
                          coa_HMAc: -1.0,
                          pi_HMAc: 1.0,
                          succ_HMAc: -1.0,
                          succoa_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# SUCD1
reaction = Reaction('HMA_SUCD1')
reaction.name = 'HMA: Succinate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({fad_HMAc: -1.0,
                          fadh2_HMAc: 1.0,
                          fum_HMAc: 1.0,
                          succ_HMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FUM
reaction = Reaction('HMA_FUM')
reaction.name = 'HMA: Fumarase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({fum_HMAc: -1.0,
                          h2o_HMAc: -1.0,
                          mal__L_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# mDH
reaction = Reaction('HMA_mDH')
reaction.name = 'HMA: Malate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({mal__L_HMAc: -1.0,
                          nad_HMAc: -1.0,
                          oaa_HMAc: 1.0,
                          nadh_HMAc: 1.0,
                          h_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# iCL
reaction = Reaction('HMA_HMAiCL')
reaction.name = 'HMA: Isocitrate lyase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({icit_HMAc: -1.0,
                          glx_HMAc: 1.0,
                          succ_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# mALS
reaction = Reaction('HMA_mALS')
reaction.name = 'HMA: Malate synthase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_HMAc: -1.0,
                          glx_HMAc: -1.0,
                          h2o_HMAc: -1.0,
                          coa_HMAc: 1.0,
                          h_HMAc: 1.0,
                          mal__L_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ATP SYNTHASE 4
reaction = Reaction('HMA_ATPS4')
reaction.name = 'HMA: ATP Synthase'
reaction.subsystem = 'Electron Transport Chain'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({adp_HMAc: -1.0,
                          pi_HMAc: -1.0,
                          h_HMAc: 3.0,
                          h2o_HMAc: 1.0,
                          h_HMAi: -4.0,
                          atp_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ATP HYDROLYSIS
reaction = Reaction('HMA_ATPHydr')
reaction.name = 'HMA: ATP Hydrolysis'
reaction.subsystem = 'ATP Demand'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({atp_HMAc: -1.0,
                          pi_HMAc: 1.0,
                          h_HMAc: 1.0,
                          h2o_HMAc: -1.0,
                          adp_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PENTOSE PHOSPHATE PATHWAY

# G6PDH2r
reaction = Reaction('HMA_G6PDH2r')
reaction.name = 'HMA: Glucose 6-phosphate dehydrogenase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g6p_HMAc: -1.0,
                          nadp_HMAc: -1.0,
                          _6pgl_HMAc: 1.0,
                          h_HMAc: 1.0,
                          nadph_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PGL
reaction = Reaction('HMA_PGL')
reaction.name = 'HMA: 6-phosphogluconolactonase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({_6pgl_HMAc: -1.0,
                          h2o_HMAc: -1.0,
                          _6pgc_HMAc: 1.0,
                          h_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# GND
reaction = Reaction('HMA_GND')
reaction.name = 'HMA: Phosphogluconate dehydrogenase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({_6pgc_HMAc: -1.0,
                          nadp_HMAc: -1.0,
                          ru5p__D_HMAc: 1.0,
                          co2_HMAc: 1.0,
                          nadph_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# RPE
reaction = Reaction('HMA_RPE')
reaction.name = 'HMA: Ribulose 5-phosphate 3-epimerase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({ru5p__D_HMAc: -1.0,
                          xu5p__D_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# RPI
reaction = Reaction('HMA_RPI')
reaction.name = 'HMA: Ribose-5-phosphate isomerase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({r5p_HMAc: 1.0,
                          xu5p__D_HMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TKT1
reaction = Reaction('HMA_TKT1')
reaction.name = 'HMA: Transketolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({r5p_HMAc: -1.0,
                          xu5p__D_HMAc: -1.0,
                          g3p_HMAc: 1.0,
                          s7p_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TALA
reaction = Reaction('HMA_TALA')
reaction.name = 'HMA: Transaldolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g3p_HMAc: -1.0,
                          s7p_HMAc: -1.0,
                          e4p_HMAc: 1.0,
                          f6p_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TKT2
reaction = Reaction('HMA_TKT2')
reaction.name = 'HMA: Transketolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({e4p_HMAc: -1.0,
                          xu5p__D_HMAc: -1.0,
                          g3p_HMAc: 1.0,
                          f6p_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# NADPH - NADH CONVERSION

# THD
reaction = Reaction('HMA_THD')
reaction.name = 'HMA: NADPH Transhydorgenase'
reaction.subsystem = 'NADPH - NADH Conversion'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({nadh_HMAc: -1.0,
                          nadp_HMAc: -1.0,
                          h_HMAi: -1.0,
                          h_HMAc: 1.0,
                          nadph_HMAc: 1.0,
                          nad_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACETATE METABOLISM

# PTAr
reaction = Reaction('HMA_PTAr')
reaction.name = 'HMA: Acetate metabolism'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_HMAc: -1.0,
                          pi_HMAc: -1.0,
                          actp_HMAc: 1.0,
                          coa_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACKr
reaction = Reaction('HMA_ACKr')
reaction.name = 'HMA: Acetate kinase'
reaction.subsystem = 'Acetate metabolism'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({ac_HMAc: 1.0,
                          atp_HMAc: 1.0,
                          actp_HMAc: -1.0,
                          adp_HMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# DIPHOSPHATE HYDROLYSIS

# PPA
reaction = Reaction('HMA_PPA')
reaction.name = 'HMA: Inorganic diphosphatase'
reaction.subsystem = 'Diphosphate hydrolysis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h2o_HMAc: -1.0,
                          ppi_HMAc: -1.0,
                          h_HMAc: 1.0,
                          pi_HMAc: 2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# AMP RECYCLING

# ADK1
reaction = Reaction('HMA_ADK1')
reaction.name = 'HMA: Adenylate kinase'
reaction.subsystem = 'AMP Recycling'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({amp_HMAc: -1.0,
                          atp_HMAc: -1.0,
                          adp_HMAc: 2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))


# BIOMASS RXN

# BIOMASS
reaction = Reaction('HMA_BIOMASS')
reaction.name = 'HMA: Biomass'
reaction.subsystem = 'Biomass'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({akg_HMAc: -1.17,
                          oaa_HMAc: -2.06,
                          g6p_HMAc: -0.26,
                          g3p_HMAc: -1.58,
                          _3pg_HMAc: -1.31,
                          pyr_HMAc: -4.33,
                          pep_HMAc: -0.92,
                          accoa_HMAc: -3.06,
                          e4p_HMAc: -0.40,
                          r5p_HMAc: -0.35,
                          fum_HMAc: 0.37,
                          ac_HMAc: 0.43,
                          for_HMAc: 0.29,
                          atp_HMAc: -36.0,
                          nadph_HMAc: -19.39,
                          nadh_HMAc: 1.10,
                          nh4_HMAc: -8.62,
                          h_HMAc: 10.13,
                          adp_HMAc: 34.6,
                          pi_HMAc: 31.88,
                          ppi_HMAc: 4.74,
                          amp_HMAc: 1.4,
                          co2_HMAc: 3.54,
                          h2o_HMAc: -7.57,
                          coa_HMAc: 3.06,
                          nad_HMAc: -1.10,
                          nadp_HMAc: 19.39,
                          so4_HMAc: -0.21,
                          biomass_HMAc: 1.0,
                          biomass_COMMUNITY: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# CODHr
reaction = Reaction('HMA_CODHr')
reaction.name = 'HMA: CODHr'
reaction.subsystem = 'HMA'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_HMAc: -1.0,
                          co2_HMAc: 1.0,
                          coa_HMAc: 1.0,
                          h_HMAc: 2.0,
                          h2o_HMAc: -1.0,
                          fdox_HMAc: -2.0,
                          fdred_HMAc: 2.0,
                          h4spt_HMAc: -1.0,
                          mh4spt_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PPCK
reaction = Reaction('HMA_PPCK')
reaction.name = 'HMA: PPCK'
reaction.subsystem = 'HMA'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({atp_HMAc: -1.0,
                          adp_HMAc: 1.0,
                          co2_HMAc: 1.0,
                          oaa_HMAc: -1.0,
                          pep_HMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

#TRANSPORT RXNS
reaction = Reaction('HMA_Transport_H2')
reaction.name = 'HMA: Transport - H2'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({h2_HMAc: 1.0,
                          h2_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_Acetate')
reaction.name = 'HMA: Transport-Acetate'
reaction.lower_bound = 0.
reaction.upper_bound = 0.
reaction.add_metabolites({ac_HMAc: 1.0,
                          ac_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_h2o')
reaction.name = 'HMA: Transport - h2o'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h2o_HMAc: 1.0,
                          h2o_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_pi')
reaction.name = 'HMA: Transport - pi'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({pi_HMAc: 1.0,
                          pi_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_ppi')
reaction.name = 'HMA: Transport - ppi'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({ppi_HMAc: 1.0,
                          ppi_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_biomass')
reaction.name = 'HMA: Transport - biomass'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({biomass_HMAc: 1.0,
                          biomass_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_co2')
reaction.name = 'HMA: Transport - co2'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({co2_HMAc: 1.0,
                          co2_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_nh4')
reaction.name = 'HMA: Transport - nh4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({nh4_HMAc: 1.0,
                          nh4_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_so4')
reaction.name = 'HMA: Transport - so4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({so4_HMAc: 1.0,
                          so4_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_for')
reaction.name = 'HMA: Transport - for'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({for_HMAc: 1.0,
                          for_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_fum')
reaction.name = 'HMA: Transport - fum'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({fum_HMAc: 1.0,
                          fum_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_lac')
reaction.name = 'HMA: Transport - lac'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({lac__D_HMAc: 1.0,
                          lac__D_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_h')
reaction.name = 'HMA: Transport - h'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h_HMAc: 1.0,
                          h_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('HMA_Transport_cH4')
reaction.name = 'HMA: Transport - cH4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({ch4_HMAc: 1.0,
                          ch4_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# METHANE EXCHANGE
reaction = Reaction('EX_CH4')
reaction.name = 'Exchange - METHANE'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({ch4_e: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))


####AMAs

pyr_AMAc = Metabolite('pyr_AMAc', formula='C3H3O3', name='Pyruvate', compartment='AMAc', charge=-1)
amp_AMAc = Metabolite('amp_AMAc', formula='C10H12N5O7P', name='AMP', compartment='AMAc', charge=-2)
cit_AMAc = Metabolite('cit_AMAc', formula='C6H5O7', name='Citrate', compartment='AMAc', charge=-3)
oaa_AMAc = Metabolite('oaa_AMAc', formula='C4H2O5', name='Oxaloacetate', compartment='AMAc', charge=-2)
_6pgl_AMAc = Metabolite('_6pgl_AMAc', formula='C6H9O9P', name='6-phospho-D-glucono-1,5-lactone', compartment='AMAc',charge=-2)
nadp_AMAc = Metabolite('nadp_AMAc', formula='C21H25N7O17P3', name='Nicotinamide adenine dinucleotide phosphate',compartment='AMAc', charge=-3)
nadph_AMAc = Metabolite('nadph_AMAc', formula='C21H26N7O17P3',name='Nicotinamide adenine dinucleotide phosphate - reduced', compartment='AMAc', charge=-4)
glx_AMAc = Metabolite('glx_AMAc', formula='C2HO3', name='Glyoxylate', compartment='CELLc', charge=-1)
fum_AMAc = Metabolite('fum_AMAc', formula='C4H2O4', name='Fumarate', compartment='AMAc', charge=-2)
mal__L_AMAc = Metabolite('mal__L_AMAc', formula='C4H4O5', name='L-Malate', compartment='AMAc', charge=-2)
fad_AMAc = Metabolite('fad_AMAc', formula='C27H31N9O15P2', name='Flavin adenine dinucleotide oxidized', compartment='AMAc', charge=-2)
fadh2_AMAc = Metabolite('fadh2_AMAc', formula='C27H33N9O15P2', name='Flavin adenine dinucleotide reduced',compartment='AMAc', charge=-2)
succ_AMAc = Metabolite('succ_AMAc', formula='C4H4O4', name='Succinate', compartment='AMAc', charge=-2)
succoa_AMAc = Metabolite('succoa_AMAc', formula='C25H35N7O19P3S', name='Succinyl-CoA', compartment='AMAc', charge=-5)
akg_AMAc = Metabolite('akg_AMAc', formula='C5H4O5', name='2-Oxoglutarate', compartment='AMAc', charge=-2)
icit_AMAc = Metabolite('icit_AMAc', formula='C6H5O7', name='Isocitrate', compartment='AMAc', charge=-3)
pep_AMAc = Metabolite('pep_AMAc', formula='C3H2O6P', name='Phosphoenolpyruvate', compartment='AMAc', charge=-3)
h2o_AMAc = Metabolite('h2o_AMAc', formula='H2O', name='H2O', compartment='AMAc', charge=0)
glc__D_AMAc = Metabolite('glc__D_AMAc', formula='C6H12O6', name='D-Glucose', compartment='AMAc', charge=0)
g6p__B_AMAc = Metabolite('g6p__B_AMAc', formula='C6H11O9P', name='B-Glucose-6-P', compartment='AMAc', charge=-2)
biomass_AMAc = Metabolite('biomass_AMAc', formula='', name='Biomass', compartment='AMAc', charge=0)
nh4_AMAc = Metabolite('nh4_AMAc', formula='NH4', name='Ammonium', compartment='AMAc', charge=1)
so4_AMAc = Metabolite('so4_AMAc', formula='O4S', name='Sulfate', compartment='AMAc', charge=-2)
for_AMAc = Metabolite('for_AMAc', formula='CHO2', name='Formate', compartment='AMAc', charge=-1)
coa_AMAc = Metabolite('coa_AMAc', formula='C21H32N7O16P3S', name='Coenzyme A', compartment='AMAc', charge=-4)
fdox_AMAc = Metabolite('fdox_AMAc', formula='Fe8S8X', name='Ferredoxin-oxidized', compartment='AMAc', charge=0)
fdred_AMAc = Metabolite('fdred_AMAc', formula='Fe8S8X', name='Ferredoxin-reduced', compartment='AMAc', charge=-2)
accoa_AMAc = Metabolite('accoa_AMAc', formula='C23H34N7O17P3S', name='Acetyl-CoA', compartment='AMAc', charge=-4)
co2_AMAc = Metabolite('co2_AMAc', formula='CO2', name='CO2', compartment='AMAc', charge=0)
h_AMAc = Metabolite('h_AMAc', formula='H', name='H+', compartment='AMAc', charge=1)
h_AMAi = Metabolite('h_AMAi', formula='H', name='h_AMAi', compartment='i', charge=1)
h2_AMAc = Metabolite('h2_AMAc', formula='H2', name='Hydrogen', compartment='AMAc', charge=0)
ac_AMAc = Metabolite('ac_AMAc', formula='C2H3O2', name='Acetate', compartment='AMAc', charge=-1)
actp_AMAc = Metabolite('actp_AMAc', formula='C2H3O5P', name='Acetyl Phosphate', compartment='AMAc', charge=-2)
adp_AMAc = Metabolite('adp_AMAc', formula='C10H12N5O10P2', name='ADP C10H12N5O10P2', compartment='AMAc', charge=-3)
atp_AMAc = Metabolite('atp_AMAc', formula='C10H12N5O13P3', name='ATP C10H12N5O13P3', compartment='AMAc', charge=-4)
pi_AMAc = Metabolite('pi_AMAc', formula='HO4P', name='Phosphate', compartment='AMAc', charge=-2)
co_AMAc = Metabolite('co_AMAc', formula='CO', name='Carbon Monoxide', compartment='AMAc', charge=0)
fdxo_42_AMAc = Metabolite('fdxo_42_AMAc', formula='Fe12S12X', name='Ferredoxin - oxidized', compartment='AMAc',charge=0)
fdxr_42_AMAc = Metabolite('fdxr_42_AMAc', formula='Fe12S12X', name='Ferredoxin - reduced', compartment='AMAc',charge=-3)
g6p_AMAc = Metabolite('g6p_AMAc', formula='C6H11O9P', name='Glucose-6-P', compartment='AMAc', charge=-2)
f6p_AMAc = Metabolite('f6p_AMAc', formula='C6H11O9P', name='Fructose-6-P', compartment='AMAc', charge=-2)
fdp_AMAc = Metabolite('fdp_AMAc', formula='C6H10O12P2', name='D-Fructose 1,6-bisphosphate', compartment='AMAc',charge=-4)
dhap_AMAc = Metabolite('dhap_AMAc', formula='C3H5O6P', name='Dihydroxyacetone phosphate', compartment='AMAc', charge=-2)
g3p_AMAc = Metabolite('g3p_AMAc', formula='C3H5O6P', name='Glyceraldehyde 3-phosphate', compartment='AMAc', charge=-2)
nad_AMAc = Metabolite('nad_AMAc', formula='C21H26N7O14P2', name='Nicotinamide adenine dinucleotide', compartment='AMAc',charge=-1)
nadh_AMAc = Metabolite('nadh_AMAc', formula='C21H27N7O14P2', name='Nicotinamide adenine dinucleotide - reduced',compartment='AMAc', charge=-2)
_13dpg_AMAc = Metabolite('_13dpg_AMAc', formula='C3H4O10P2', name='3-Phospho-D-glyceroyl phosphate', compartment='AMAc',charge=-4)
_3pg_AMAc = Metabolite('_3pg_AMAc', formula='C3H4O7P', name='3-Phospho-D-glycerate', compartment='AMAc', charge=-3)
_2pg_AMAc = Metabolite('_2pg_AMAc', formula='C3H4O7P', name='2-Phospho-D-glycerate', compartment='AMAc', charge=-3)
lac__D_AMAc = Metabolite('lac__D_AMAc', formula='C3H5O3', name='D-Lactate', compartment='CELLc', charge=-1)
ppi_AMAc = Metabolite('ppi_AMAc', formula='HO7P2', name='Diphosphate', compartment='AMAc', charge=-3)
e4p_AMAc = Metabolite('e4p_AMAc', formula='C4H7O7P', name='D-Erythrose 4-phosphate', compartment='AMAc', charge=-2)
s7p_AMAc = Metabolite('s7p_AMAc', formula='C7H13O10P', name='Sedoheptulose 7-phosphate', compartment='AMAc', charge=-2)
r5p_AMAc = Metabolite('r5p_AMAc', formula='C5H9O8P', name='Alpha-D-Ribose 5-phosphate', compartment='AMAc', charge=-2)
xu5p__D_AMAc = Metabolite('xu5p__D_AMAc', formula='C5H9O8P', name='D-Xylulose 5-phosphate', compartment='AMAc', charge=-2)
ru5p__D_AMAc = Metabolite('ru5p__D_AMAc', formula='C5H9O8P', name='D-Ribulose 5-phosphate', compartment='AMAc',charge=-2)
_6pgc_AMAc = Metabolite('_6pgc_AMAc', formula='C6H10O10P', name='6-Phospho-D-gluconate', compartment='AMAc', charge=-3)
glc__D_e = Metabolite('glc__D_e', formula='C6H12O6', name='D-Glucose', compartment='e', charge=0)
h2o_e = Metabolite('h2o_e', formula='H2O', name='H2O', compartment='e', charge=0)
pi_e = Metabolite('pi_e', formula='HO4P', name='Phosphate', compartment='e', charge=-2)
ppi_e = Metabolite('ppi_e', formula='HO7P2', name='Diphosphate', compartment='e', charge=-3)
biomass_e = Metabolite('biomass_e', formula='', name='Biomass_e', compartment='e', charge=0)
co2_e = Metabolite('co2_e', formula='CO2', name='CO2', compartment='e', charge=0)
nh4_e = Metabolite('nh4_e', formula='NH4', name='Ammonium', compartment='e', charge=1)
so4_e = Metabolite('so4_e', formula='O4S', name='Sulfate', compartment='e', charge=-2)
for_e = Metabolite('for_e', formula='CHO2', name='Formate', compartment='e', charge=-1)
fum_e = Metabolite('fum_e', formula='C4H2O4', name='Fumarate', compartment='e', charge=-2)
lac__D_e = Metabolite('lac__D_e', formula='C3H5O3', name='D-Lactate', compartment='e', charge=-1)
h_e = Metabolite('h_e', formula='H', name='H+', compartment='e', charge=1)
ac_e = Metabolite('ac_e', formula='C2H3O2', name='Acetate', compartment='e', charge=-1)
mfr_b_AMAc = Metabolite('mfr_b_AMAc', formula='C34H44N6O14', name='A Methanofuran', compartment='AMAc', charge=0)
formmfr_b_AMAc = Metabolite('formmfr_b_AMAc', formula='C35H43N4O15R', name='A Formylmethanofuran', compartment='AMAc',charge=0)
formh4spt_AMAc = Metabolite('formh4spt_AMAc', formula='C36H48N7O20P1', name='Formyltetrahydrosarcinapterin', compartment='AMAc', charge=0)
h4spt_AMAc = Metabolite('h4spt_AMAc', formula='C35H48N7O19P1', name='Tetrahydrosarcinapterin', compartment='AMAc',charge=0)
menylh4spt_AMAc = Metabolite('menylh4spt_AMAc', formula='C36H47N7O19P1', name='Methenyl-tetrahydrosarcinapterin',compartment='AMAc', charge=0)
f420_2_AMAc = Metabolite('f420_2_AMAc', name='Coenzyme ferredoxin 420-2 (oxidized)', formula='C29H34N5O18P',compartment='AMAc', charge=0)
f420_2h2_AMAc = Metabolite('f420_2h2_AMAc', name='Coenzyme ferredoxin 420-2 (reduced)', formula='C29H36O18N5P1',compartment='AMAc', charge=0)
mleneh4spt_AMAc = Metabolite('mleneh4spt_AMAc', name='N5,N10-methylee-5,6,7,8-tetrahydromethanopterin', formula='C36H48N7O19P1', compartment='AMAc', charge=0)
com_AMAc = Metabolite('com_AMAc', name='Coenzyme m', formula='C2H5O3S2', compartment='AMAc', charge=0)
mcom_AMAc = Metabolite('mcom_AMAc', name='Methylcoenzyme m', formula='C3O3S2H7', compartment='AMAc', charge=0)
mphen_AMAc = Metabolite('mphen_AMAc', name='Methanophenazine (oxidized)', formula='C37N2O1H50', compartment='AMAc',charge=0)
mphenh2_AMAc = Metabolite('mphenh2_AMAc', name='Methanophenazine (reduced)', formula='C37N2O1H52', compartment='AMAc',charge=0)
h2_e = Metabolite('h2_e', name='Hydrogen', formula='H2', compartment='e', charge=0)
mh4spt_AMAc = Metabolite('mh4spt_AMA', name='N5-methyl-tetrahydrosarcinapterin', formula='C36H50N7O19P1',compartment='AMAc', charge=0)
ch4_e = Metabolite('ch4_e', formula='CH4', name='Methane', compartment='e', charge=0)
ch4_AMAc = Metabolite('ch4_AMAc', formula='CH4', name='Methane', compartment='AMAc', charge=0)
cob_AMAc = Metabolite('cob_AMAc', formula='C11H19N1O7P1S1', name='Conenzyme B', compartment='AMAc', charge=0)
hsfd_AMAc = Metabolite('hsfd_AMAc', formula='C13H22N1O10P1S3', name='Heterodisulfide', compartment='AMAc', charge=0)

# AMA RXN's from Fig 3

#accoa_c + h2o_c + 2.0 fdox_c + h4spt_c <-> co2_c + coa_c + 2.0 h_c + 2.0 fdred_c + mh4spt_c
reaction = Reaction('AMA_CODHr')
reaction.name = 'AMA: CODHr'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_AMAc: -1.0,
                          h2o_AMAc: -1.0,
                          fdox_AMAc: -2.0,
                          h4spt_AMAc: -1.0,
                          co2_AMAc: 1.0,
                          coa_AMAc: 1.0,
                          h_AMAc: 2.0,
                          fdred_AMAc: 2.0,
                          mh4spt_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))


# MTSPCMMT [6]
reaction = Reaction('AMA_MTSPCMMT')
reaction.name = 'AMA: MTSPCMMT'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_AMAc: -1.7,
                          h_AMAi: 1.7,
                          h4spt_AMAc: 1.0,
                          mh4spt_AMAc: -1.0,
                          com_AMAc: -1.0,
                          mcom_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ION MOTIVE FORCE

# F4D (not shown in Fig 3???)
reaction = Reaction('AMA_F4D')
reaction.name = 'AMA: F4D'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_AMAc: -1.8,
                          f420_2h2_AMAc: -1.0,
                          mphen_AMAc: -1.0,
                          h_AMAi: 1.8,
                          f420_2_AMAc: 1.0,
                          mphenh2_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# F4NH (not shown in Fig 3??)
reaction = Reaction('AMA_F4NH')
reaction.name = 'AMA: F4NH'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_AMAc: -1.8,
                          h_AMAi: 1.8,
                          h2_AMAc: -1.0,
                          mphen_AMAc: -1.0,
                          mphenh2_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# MCR
reaction = Reaction('AMA_MCR')
reaction.name = 'AMA: MCR'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({ch4_AMAc: 1.0,
                          cob_AMAc: -1.0,
                          mcom_AMAc: -1.0,
                          hsfd_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# HDR
reaction = Reaction('AMA_HDR')
reaction.name = 'AMA: HDR'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_AMAc: -1.8,
                          h_AMAi: 1.8,
                          cob_AMAc: 1.0,
                          com_AMAc: 1.0,
                          mphen_AMAc: 1.0,
                          mphenh2_AMAc: -1.0,
                          hsfd_AMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ECHH_10
reaction = Reaction('AMA_ECHH_10')
reaction.name = 'AMA: ECHH 10'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({h_AMAc: -3.0,
                          h2_AMAc: 1.0,
                          h_AMAi: 1.0,
                          fdox_AMAc: 2.0,
                          fdred_AMAc: -2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# I got rid of Glycolysis, Upper Glycolysis, and Lower Glycolysis
# DO I NEED GLUCONEOGENESIS RXN PPS?? WHERE IS THE PYRUVATE COMING FROM??
# I KEPT ATP SYNTHASE, BUT DO I NEED TO KEEP ATP HYDROLYSIS?
# should i keep: DIPHOSPHATE HYDROLYSIS, ACETATE METABOLISM, NADPH - NADH CONVERSION
# should i keep: RNF complex, AMP RECYCLING, LACTATE METABOLISM
# I don't have the electron transport chain anywhere, that's ok right
# I never produce lactate in gfo's, right? can i just delete lactate metabolism

# GLUCONEOGENESIS

##AMY- I ADDED A BUNCH OF REACTIONS BELOW FOR GLUCONEOGENESIS
##THESE ARE THE REVERSIBLE GLYCOLYSIS REACTIONS AND ALLOW
##FOR BIOMASS PRECURSORS TO BE PRODUCED

g6p_AMAc = Metabolite('g6p_AMAc', formula='C6H11O9P', name='Glucose-6-P', compartment='AMAc', charge=-2)

reaction = Reaction('AMA_G6PI')
reaction.name = 'AMA: Glucose 6 phosphate isomerase - 1'
reaction.subsystem = 'Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({g6p_AMAc: -1,
                          g6p__B_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Glucose 6 phosphate isomerase - 2
# g6p_AMAc <-> f6p_AMAc
f6p_AMAc = Metabolite('f6p_AMAc', formula='C6H11O9P', name='Fructose-6-P', compartment='AMAc', charge=-2)

reaction = Reaction('AMA_PGI')
reaction.name = 'AMA: Glucose 6 phosphate isomerase - 2'
reaction.subsystem = 'Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({g6p_AMAc: -1,
                          f6p_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))


# Fructose-bisphosphate aldolase
# fdp_AMAc <-> dhapLc + g3p_AMAc
dhap_AMAc = Metabolite('dhap_AMAc', formula='C3H5O6P', name='Dihydroxyacetone phosphate', compartment='AMAc', charge=-2)
g3p_AMAc = Metabolite('g3p_AMAc', formula='C3H5O6P', name='Glyceraldehyde 3-phosphate', compartment='AMAc', charge=-2)

reaction = Reaction('AMA_FBA')
reaction.name = 'AMA: Fructose-bisphosphate aldolase'
reaction.subsystem = 'Upper Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({fdp_AMAc: -1.0,
                          dhap_AMAc: 1.0,
                          g3p_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Triose-phosphate isomerase
# dhap_AMAc <-> g3p_AMAc

reaction = Reaction('AMA_TPI')
reaction.name = 'AMA: Triose-phosphate isomerase'
reaction.subsystem = 'Upper Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({dhap_AMAc: -1.0,
                          g3p_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# LOWER GLYCOLYSIS

# Glyceraldehyde-3-phosphate dehydrogenase
# g3p_AMAc + nad_AMAc + pi_AMAc <-> 13dpg_AMAc + h_AMAc + nadh_AMAc
nad_AMAc = Metabolite('nad_AMAc', formula='C21H26N7O14P2', name='Nicotinamide adenine dinucleotide', compartment='AMAc',
                      charge=-1)
nadh_AMAc = Metabolite('nadh_AMAc', formula='C21H27N7O14P2', name='Nicotinamide adenine dinucleotide - reduced',
                       compartment='AMAc', charge=-2)
_13dpg_AMAc = Metabolite('_13dpg_AMAc', formula='C3H4O10P2', name='3-Phospho-D-glyceroyl phosphate', compartment='AMAc',
                         charge=-4)
pi_AMAc = Metabolite('pi_AMAc', formula='HO4P', name='Phosphate', compartment='AMAc', charge=-2)

reaction = Reaction('AMA_GAPD')
reaction.name = 'AMA: Glyceraldehyde-3-phosphate dehydrogenase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({g3p_AMAc: -1.0,
                          nad_AMAc: -1.0,
                          pi_AMAc: -1.0,
                          _13dpg_AMAc: 1.0,
                          h_AMAc: 1.0,
                          nadh_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Phosphoglycerate kinase
# 3pg_AMAc + atp_AMAc <-> 13dpg_AMAc + adp_AMAc
_3pg_AMAc = Metabolite('_3pg_AMAc', formula='C3H4O7P', name='3-Phospho-D-glycerate', compartment='AMAc', charge=-3)

reaction = Reaction('AMA_PGK')
reaction.name = 'AMA: Phosphoglycerate kinase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({_3pg_AMAc: -1.0,
                          atp_AMAc: -1.0,
                          _13dpg_AMAc: 1.0,
                          adp_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Phosphoglycerate mutase
# 2pg_AMAc <-> 3pg_AMAc
_2pg_AMAc = Metabolite('_2pg_AMAc', formula='C3H4O7P', name='2-Phospho-D-glycerate', compartment='AMAc', charge=-3)

reaction = Reaction('AMA_PGM')
reaction.name = 'AMA: Phosphoglycerate mutase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({_2pg_AMAc: -1.0,
                          _3pg_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Enolase
# 2pg_AMAc <-> h2o_AMAc + pep_AMAc
pep_AMAc = Metabolite('pep_AMAc', formula='C3H2O6P', name='Phosphoenolpyruvate', compartment='AMAc', charge=-3)
h2o_AMAc = Metabolite('h2o_AMAc', formula='H2O', name='H2O', compartment='AMAc', charge=0)

reaction = Reaction('AMA_ENO')
reaction.name = 'AMA: Enolase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = -1000.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({_2pg_AMAc: -1.0,
                          h2o_AMAc: 1.0,
                          pep_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# Pyruvate kinase
# adp_AMAc + h_AMAc + pep_AMAc <-> atp_AMAc + pyr_AMAc
pyr_AMAc = Metabolite('pyr_AMAc', formula='C3H3O3', name='Pyruvate', compartment='AMAc', charge=-1)

reaction = Reaction('AMA_PYK')
reaction.name = 'AMA: Pyruvate kinase'
reaction.subsystem = 'Lower Glycolysis'
reaction.lower_bound = 0.  # This is the default
reaction.upper_bound = 1000.  # This is the default

reaction.add_metabolites({adp_AMAc: -1.0,
                          h_AMAc: -1.0,
                          pep_AMAc: -1.0,
                          atp_AMAc: 1.0,
                          pyr_AMAc: 1.0})

model.add_reactions([reaction])

print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PPS
reaction = Reaction('AMA_PPS')
reaction.name = 'AMA: Phosphoenolpyruvate synthase'
reaction.subsystem = 'Gluconeogenesis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({atp_AMAc: -1.0,
                          h2o_AMAc: -1.0,
                          pyr_AMAc: -1.0,
                          amp_AMAc: 1.0,
                          h_AMAc: 2.0,
                          pep_AMAc: 1.0,
                          pi_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FBP
reaction = Reaction('AMA_FBP')
reaction.name = 'AMA: Fructose-bisphosphatase'
reaction.subsystem = 'Gluconeogenesis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({fdp_AMAc: -1.0,
                          h2o_AMAc: -1.0,
                          f6p_AMAc: 1.0,
                          pi_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TCA CYCLE

# CS
reaction = Reaction('AMA_CS')
reaction.name = 'AMA: Citrate synthase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_AMAc: -1.0,
                          h2o_AMAc: -1.0,
                          oaa_AMAc: -1.0,
                          cit_AMAc: 1.0,
                          coa_AMAc: 1.0,
                          h_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACONT
reaction = Reaction('AMA_ACONT')
reaction.name = 'AMA: Aconitate hydratase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({cit_AMAc: -1.0,
                          icit_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# iCDHx
reaction = Reaction('AMA_AMAiCDHx')
reaction.name = 'AMA: Isocitrate dehydrogenase (NAD)'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({icit_AMAc: -1.0,
                          nad_AMAc: -1.0,
                          akg_AMAc: 1.0,
                          co2_AMAc: 1.0,
                          nadh_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# AKGDH
reaction = Reaction('AMA_AKGDH')
reaction.name = 'AMA: 2-Oxoglutarate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({akg_AMAc: -1.0,
                          coa_AMAc: -1.0,
                          nad_AMAc: -1.0,
                          co2_AMAc: 1.0,
                          nadh_AMAc: 1.0,
                          succoa_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# SUCOAS
reaction = Reaction('AMA_SUCOAS')
reaction.name = 'AMA: Succinyl-CoA synthetase (ADP-forming)'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({adp_AMAc: 1.0,
                          atp_AMAc: -1.0,
                          coa_AMAc: -1.0,
                          pi_AMAc: 1.0,
                          succ_AMAc: -1.0,
                          succoa_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# SUCD1
reaction = Reaction('AMA_SUCD1')
reaction.name = 'AMA: Succinate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({fad_AMAc: -1.0,
                          fadh2_AMAc: 1.0,
                          fum_AMAc: 1.0,
                          succ_AMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# FUM
reaction = Reaction('AMA_FUM')
reaction.name = 'AMA: Fumarase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({fum_AMAc: -1.0,
                          h2o_AMAc: -1.0,
                          mal__L_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# mDH
reaction = Reaction('AMA_mDH')
reaction.name = 'AMA: Malate dehydrogenase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({mal__L_AMAc: -1.0,
                          nad_AMAc: -1.0,
                          oaa_AMAc: 1.0,
                          nadh_AMAc: 1.0,
                          h_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# iCL
reaction = Reaction('AMA_AMAiCL')
reaction.name = 'AMA: Isocitrate lyase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({icit_AMAc: -1.0,
                          glx_AMAc: 1.0,
                          succ_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# mALS
reaction = Reaction('AMA_mALS')
reaction.name = 'AMA: Malate synthase'
reaction.subsystem = 'TCA Cycle'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_AMAc: -1.0,
                          glx_AMAc: -1.0,
                          h2o_AMAc: -1.0,
                          coa_AMAc: 1.0,
                          h_AMAc: 1.0,
                          mal__L_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ATP SYNTHASE 4
reaction = Reaction('AMA_ATPS4')
reaction.name = 'AMA: ATP Synthase'
reaction.subsystem = 'Electron Transport Chain'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({adp_AMAc: -1.0,
                          pi_AMAc: -1.0,
                          h_AMAc: 3.0,
                          h2o_AMAc: 1.0,
                          h_AMAi: -4.0,
                          atp_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ATP HYDROLYSIS
reaction = Reaction('AMA_ATPHydr')
reaction.name = 'AMA: ATP Hydrolysis'
reaction.subsystem = 'ATP Demand'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({atp_AMAc: -1.0,
                          pi_AMAc: 1.0,
                          h_AMAc: 1.0,
                          h2o_AMAc: -1.0,
                          adp_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PENTOSE PHOSPHATE PATHWAY

# G6PDH2r
reaction = Reaction('AMA_G6PDH2r')
reaction.name = 'AMA: Glucose 6-phosphate dehydrogenase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g6p_AMAc: -1.0,
                          nadp_AMAc: -1.0,
                          _6pgl_AMAc: 1.0,
                          h_AMAc: 1.0,
                          nadph_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PGL
reaction = Reaction('AMA_PGL')
reaction.name = 'AMA: 6-phosphogluconolactonase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({_6pgl_AMAc: -1.0,
                          h2o_AMAc: -1.0,
                          _6pgc_AMAc: 1.0,
                          h_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# GND
reaction = Reaction('AMA_GND')
reaction.name = 'AMA: Phosphogluconate dehydrogenase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({_6pgc_AMAc: -1.0,
                          nadp_AMAc: -1.0,
                          ru5p__D_AMAc: 1.0,
                          co2_AMAc: 1.0,
                          nadph_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# RPE
reaction = Reaction('AMA_RPE')
reaction.name = 'AMA: Ribulose 5-phosphate 3-epimerase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({ru5p__D_AMAc: -1.0,
                          xu5p__D_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# RPI
reaction = Reaction('AMA_RPI')
reaction.name = 'AMA: Ribose-5-phosphate isomerase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({r5p_AMAc: 1.0,
                          xu5p__D_AMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TKT1
reaction = Reaction('AMA_TKT1')
reaction.name = 'AMA: Transketolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({r5p_AMAc: -1.0,
                          xu5p__D_AMAc: -1.0,
                          g3p_AMAc: 1.0,
                          s7p_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TALA
reaction = Reaction('AMA_TALA')
reaction.name = 'AMA: Transaldolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({g3p_AMAc: -1.0,
                          s7p_AMAc: -1.0,
                          e4p_AMAc: 1.0,
                          f6p_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# TKT2
reaction = Reaction('AMA_TKT2')
reaction.name = 'AMA: Transketolase'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({e4p_AMAc: -1.0,
                          xu5p__D_AMAc: -1.0,
                          g3p_AMAc: 1.0,
                          f6p_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# NADPH - NADH CONVERSION

# THD
reaction = Reaction('AMA_THD')
reaction.name = 'AMA: NADPH Transhydorgenase'
reaction.subsystem = 'NADPH - NADH Conversion'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({nadh_AMAc: -1.0,
                          nadp_AMAc: -1.0,
                          h_AMAi: -1.0,
                          h_AMAc: 1.0,
                          nadph_AMAc: 1.0,
                          nad_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACETATE METABOLISM

# PTAr
reaction = Reaction('AMA_PTAr')
reaction.name = 'AMA: Acetate metabolism'
reaction.subsystem = 'Pentose Phosphate Pathway'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({accoa_AMAc: -1.0,
                          pi_AMAc: -1.0,
                          actp_AMAc: 1.0,
                          coa_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# ACKr
reaction = Reaction('AMA_ACKr')
reaction.name = 'AMA: Acetate kinase'
reaction.subsystem = 'Acetate metabolism'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({ac_AMAc: 1.0,
                          atp_AMAc: 1.0,
                          actp_AMAc: -1.0,
                          adp_AMAc: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# DIPHOSPHATE HYDROLYSIS

# PPA
reaction = Reaction('AMA_PPA')
reaction.name = 'AMA: Inorganic diphosphatase'
reaction.subsystem = 'Diphosphate hydrolysis'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({h2o_AMAc: -1.0,
                          ppi_AMAc: -1.0,
                          h_AMAc: 1.0,
                          pi_AMAc: 2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# AMP RECYCLING

# ADK1
reaction = Reaction('AMA_ADK1')
reaction.name = 'AMA: Adenylate kinase'
reaction.subsystem = 'AMP Recycling'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({amp_AMAc: -1.0,
                          atp_AMAc: -1.0,
                          adp_AMAc: 2.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# BIOMASS RXN

# BIOMASS
reaction = Reaction('AMA_BIOMASS')
reaction.name = 'AMA: Biomass'
reaction.subsystem = 'Biomass'
reaction.lower_bound = 0.
reaction.upper_bound = 1000.

reaction.add_metabolites({akg_AMAc: -1.17,
                          oaa_AMAc: -2.06,
                          g6p_AMAc: -0.26,
                          g3p_AMAc: -1.58,
                          _3pg_AMAc: -1.31,
                          pyr_AMAc: -4.33,
                          pep_AMAc: -0.92,
                          accoa_AMAc: -3.06,
                          e4p_AMAc: -0.40,
                          r5p_AMAc: -0.35,
                          fum_AMAc: 0.37,
                          ac_AMAc: 0.43,
                          for_AMAc: 0.29,
                          atp_AMAc: -36.0,
                          nadph_AMAc: -19.39,
                          nadh_AMAc: 1.10,
                          nh4_AMAc: -8.62,
                          h_AMAc: 10.13,
                          adp_AMAc: 34.6,
                          pi_AMAc: 31.88,
                          ppi_AMAc: 4.74,
                          amp_AMAc: 1.4,
                          co2_AMAc: 3.54,
                          h2o_AMAc: -7.57,
                          coa_AMAc: 3.06,
                          nad_AMAc: -1.10,
                          nadp_AMAc: 19.39,
                          so4_AMAc: -0.21,
                          biomass_AMAc: 1.0,
                          biomass_COMMUNITY: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# PPCK
reaction = Reaction('AMA_PPCK')
reaction.name = 'AMA: PPCK'
reaction.subsystem = 'AMA'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.

reaction.add_metabolites({atp_AMAc: -1.0,
                          adp_AMAc: 1.0,
                          co2_AMAc: 1.0,
                          oaa_AMAc: -1.0,
                          pep_AMAc: 1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

# AMA -TRANSPORT RXNS !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
reaction = Reaction('AMA_Transport_H2')
reaction.name = 'AMA: Transport - H2'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h2_AMAc: 1.0,
                          h2_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_Acetate')
reaction.name = 'AMA: Transport-Acetate'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({ac_AMAc: 1.0,
                          ac_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_h2o')
reaction.name = 'AMA: Transport - h2o'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h2o_AMAc: 1.0,
                          h2o_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_pi')
reaction.name = 'AMA: Transport - pi'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({pi_AMAc: 1.0,
                          pi_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_ppi')
reaction.name = 'AMA: Transport - ppi'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({ppi_AMAc: 1.0,
                          ppi_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_biomass')
reaction.name = 'AMA: Transport - biomass'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({biomass_AMAc: 1.0,
                          biomass_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_co2')
reaction.name = 'AMA: Transport - co2'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({co2_AMAc: 1.0,
                          co2_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_nh4')
reaction.name = 'AMA: Transport - nh4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({nh4_AMAc: 1.0,
                          nh4_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_so4')
reaction.name = 'AMA: Transport - so4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({so4_AMAc: 1.0,
                          so4_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_for')
reaction.name = 'AMA: Transport - for'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({for_AMAc: 1.0,
                          for_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_fum')
reaction.name = 'AMA: Transport - fum'
reaction.lower_bound = -1000.
reaction.upper_bound = 0.
reaction.add_metabolites({fum_AMAc: 1.0,
                          fum_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_h')
reaction.name = 'AMA: Transport - h'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({h_AMAc: 1.0,
                          h_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))

reaction = Reaction('AMA_Transport_cH4')
reaction.name = 'AMA: Transport - cH4'
reaction.lower_bound = -1000.
reaction.upper_bound = 1000.
reaction.add_metabolites({ch4_AMAc: 1.0,
                          ch4_e: -1.0})
model.add_reactions([reaction])
print(reaction.name + ": " + str(reaction.check_mass_balance()))


#########################################
#########################################
#########################################

medium = model.medium

medium["EX_glc__D"] = 1
medium["EX_H2"] = 0

model.medium = medium
print(model.medium)

# Add additional constraints
model.reactions.GFO_ECH.knock_out()

model.objective = 'DEMAND_biomass_COMMUNITY'
#model.objective = 'AMA_ATPHydr'

pfba_solution = cobra.flux_analysis.pfba(model)
model.summary()
print(pfba_solution.fluxes)

pfba_solution.fluxes.to_json("fluxes.json")

workbook = xlsxwriter.Workbook('FluxResults.xlsx')
worksheet = workbook.add_worksheet('FluxResults')

worksheet.write(0, 0, "reaction")
worksheet.write(0, 1, "flux")

row = 1
col = 0

for rxn in model.reactions:
    worksheet.write(row, col, str(rxn))
    row += 1

row = 1
col += 1

for flux in pfba_solution.fluxes:
    worksheet.write(row, col, flux)
    row += 1

workbook.close()

cobra.io.save_json_model(model, "model.json")
