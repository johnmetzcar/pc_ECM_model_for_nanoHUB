 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='initial_anisotropy', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.initial_anisotropy = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name2 = Button(description='initial_ECM_density', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.initial_ECM_density = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name3 = Button(description='cell_setup', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.cell_setup = Text(
          value='lesion',
          style=style, layout=widget_layout)

        param_name4 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.tumor_radius = FloatText(
          value=175,
          step=10,
          style=style, layout=widget_layout)

        param_name5 = Button(description='initial_leader_cell_fraction', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.initial_leader_cell_fraction = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name6 = Button(description='oxygen_uptake', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.oxygen_uptake = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name7 = Button(description='default_cell_speed', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.default_cell_speed = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name8 = Button(description='default_persistence_time', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.default_persistence_time = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name9 = Button(description='leader_adhesion', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.leader_adhesion = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='leader_repulsion', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.leader_repulsion = FloatText(
          value=25.0,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='oxygen_migration_bias_for_leaders', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.oxygen_migration_bias_for_leaders = FloatText(
          value=0.95,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='anisotropy_increase_rate', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.anisotropy_increase_rate = FloatText(
          value=0.004,
          step=0.001,
          style=style, layout=widget_layout)

        param_name13 = Button(description='fiber_realignment_rate', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.fiber_realignment_rate = FloatText(
          value=4.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name14 = Button(description='default_ECM_density_target', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.default_ECM_density_target = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='follower_adhesion', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.follower_adhesion = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='follower_repulsion', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.follower_repulsion = FloatText(
          value=25.0,
          step=1,
          style=style, layout=widget_layout)

        param_name17 = Button(description='default_chemotaxis_bias', disabled=True, layout=name_button_layout)
        param_name17.style.button_color = 'lightgreen'

        self.default_chemotaxis_bias = FloatText(
          value=0.05,
          step=0.01,
          style=style, layout=widget_layout)

        param_name18 = Button(description='default_ECM_sensitivity', disabled=True, layout=name_button_layout)
        param_name18.style.button_color = 'tan'

        self.default_ECM_sensitivity = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name19 = Button(description='rho_L', disabled=True, layout=name_button_layout)
        param_name19.style.button_color = 'lightgreen'

        self.rho_L = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name20 = Button(description='rho_H', disabled=True, layout=name_button_layout)
        param_name20.style.button_color = 'tan'

        self.rho_H = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name21 = Button(description='rho_I', disabled=True, layout=name_button_layout)
        param_name21.style.button_color = 'lightgreen'

        self.rho_I = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name22 = Button(description='default_hysteresis_bias', disabled=True, layout=name_button_layout)
        param_name22.style.button_color = 'tan'

        self.default_hysteresis_bias = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name23 = Button(description='leader_motility_mode', disabled=True, layout=name_button_layout)
        param_name23.style.button_color = 'lightgreen'

        self.leader_motility_mode = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name24 = Button(description='follower_motility_mode', disabled=True, layout=name_button_layout)
        param_name24.style.button_color = 'tan'

        self.follower_motility_mode = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        param_name25 = Button(description='chemotactic_substrate_decay_rate', disabled=True, layout=name_button_layout)
        param_name25.style.button_color = 'lightgreen'

        self.chemotactic_substrate_decay_rate = FloatText(
          value=0.1,
          step=0.01,
          style=style, layout=widget_layout)

        param_name26 = Button(description='chemical_field_setup', disabled=True, layout=name_button_layout)
        param_name26.style.button_color = 'tan'

        self.chemical_field_setup = Text(
          value='none',
          style=style, layout=widget_layout)

        param_name27 = Button(description='angle_of_chemical_field_gradient', disabled=True, layout=name_button_layout)
        param_name27.style.button_color = 'lightgreen'

        self.angle_of_chemical_field_gradient = FloatText(
          value=45.0,
          step=1,
          style=style, layout=widget_layout)

        param_name28 = Button(description='ECM_orientation_setup', disabled=True, layout=name_button_layout)
        param_name28.style.button_color = 'tan'

        self.ECM_orientation_setup = Text(
          value='random',
          style=style, layout=widget_layout)

        param_name29 = Button(description='ECM_dx', disabled=True, layout=name_button_layout)
        param_name29.style.button_color = 'lightgreen'

        self.ECM_dx = FloatText(
          value=20,
          step=1,
          style=style, layout=widget_layout)

        param_name30 = Button(description='ECM_dy', disabled=True, layout=name_button_layout)
        param_name30.style.button_color = 'tan'

        self.ECM_dy = FloatText(
          value=20,
          step=1,
          style=style, layout=widget_layout)

        param_name31 = Button(description='ECM_dz', disabled=True, layout=name_button_layout)
        param_name31.style.button_color = 'lightgreen'

        self.ECM_dz = FloatText(
          value=20,
          step=1,
          style=style, layout=widget_layout)

        param_name32 = Button(description='cell_motility_ECM_interaction_model_selector', disabled=True, layout=name_button_layout)
        param_name32.style.button_color = 'tan'

        self.cell_motility_ECM_interaction_model_selector = Text(
          value='follower chemotaxis/no follower hysteresis',
          style=style, layout=widget_layout)

        param_name33 = Button(description='discrete_ECM_remodeling', disabled=True, layout=name_button_layout)
        param_name33.style.button_color = 'lightgreen'

        self.discrete_ECM_remodeling = IntText(
          value=1,
          step=0.1,
          style=style, layout=widget_layout)

        param_name34 = Button(description='link_anisotropy_and_bias', disabled=True, layout=name_button_layout)
        param_name34.style.button_color = 'tan'

        self.link_anisotropy_and_bias = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name35 = Button(description='ecm_update_model', disabled=True, layout=name_button_layout)
        param_name35.style.button_color = 'lightgreen'

        self.ecm_update_model = Text(
          value='ecm_update_from_cell_motility_vector',
          style=style, layout=widget_layout)

        param_name36 = Button(description='normalize_ECM_influenced_motility_vector', disabled=True, layout=name_button_layout)
        param_name36.style.button_color = 'tan'

        self.normalize_ECM_influenced_motility_vector = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name37 = Button(description='duration_of_uE_conditioning', disabled=True, layout=name_button_layout)
        param_name37.style.button_color = 'lightgreen'

        self.duration_of_uE_conditioning = FloatText(
          value=10,
          step=1,
          style=style, layout=widget_layout)

        param_name38 = Button(description='freeze_uE_profile', disabled=True, layout=name_button_layout)
        param_name38.style.button_color = 'tan'

        self.freeze_uE_profile = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name39 = Button(description='unit_test_setup', disabled=True, layout=name_button_layout)
        param_name39.style.button_color = 'lightgreen'

        self.unit_test_setup = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name40 = Button(description='march_unit_test_setup', disabled=True, layout=name_button_layout)
        param_name40.style.button_color = 'tan'

        self.march_unit_test_setup = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        param_name41 = Button(description='visual_guideline_pattern', disabled=True, layout=name_button_layout)
        param_name41.style.button_color = 'lightgreen'

        self.visual_guideline_pattern = Text(
          value='none',
          style=style, layout=widget_layout)

        param_name42 = Button(description='enable_ecm_outputs', disabled=True, layout=name_button_layout)
        param_name42.style.button_color = 'tan'

        self.enable_ecm_outputs = Checkbox(
          value=True,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='microns', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='mmHg/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='microns/minute', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='minutes', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='micron/minute', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='micron/minute', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='dimenionless', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='micron/minute', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='micron/minute', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'
        units_button17 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'lightgreen'
        units_button18 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button18.style.button_color = 'tan'
        units_button19 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button19.style.button_color = 'lightgreen'
        units_button20 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button20.style.button_color = 'tan'
        units_button21 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button21.style.button_color = 'lightgreen'
        units_button22 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button22.style.button_color = 'tan'
        units_button23 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button23.style.button_color = 'lightgreen'
        units_button24 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button24.style.button_color = 'tan'
        units_button25 = Button(description='1/minutes', disabled=True, layout=units_button_layout) 
        units_button25.style.button_color = 'lightgreen'
        units_button26 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button26.style.button_color = 'tan'
        units_button27 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button27.style.button_color = 'lightgreen'
        units_button28 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button28.style.button_color = 'tan'
        units_button29 = Button(description='um', disabled=True, layout=units_button_layout) 
        units_button29.style.button_color = 'lightgreen'
        units_button30 = Button(description='um', disabled=True, layout=units_button_layout) 
        units_button30.style.button_color = 'tan'
        units_button31 = Button(description='um', disabled=True, layout=units_button_layout) 
        units_button31.style.button_color = 'lightgreen'
        units_button32 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button32.style.button_color = 'tan'
        units_button33 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button33.style.button_color = 'lightgreen'
        units_button34 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button34.style.button_color = 'tan'
        units_button35 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button35.style.button_color = 'lightgreen'
        units_button36 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button36.style.button_color = 'tan'
        units_button37 = Button(description='minutes', disabled=True, layout=units_button_layout) 
        units_button37.style.button_color = 'lightgreen'
        units_button38 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button38.style.button_color = 'tan'
        units_button39 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button39.style.button_color = 'lightgreen'
        units_button40 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button40.style.button_color = 'tan'
        units_button41 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button41.style.button_color = 'lightgreen'
        units_button42 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button42.style.button_color = 'tan'

        desc_button1 = Button(description='Initial ECM anisotropy' , tooltip='Initial ECM anisotropy', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='Initial ECM density' , tooltip='Initial ECM density', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='single, random, lesion, cells at y = 0, circle of cells, or cells at left boundary/march' , tooltip='single, random, lesion, cells at y = 0, circle of cells, or cells at left boundary/march', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='Initial cell lesion radius (lesion only)' , tooltip='Initial cell lesion radius (lesion only)', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='Average percentage of leaders initialized (lesion only)' , tooltip='Average percentage of leaders initialized (lesion only)', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='Default cell oxygen uptake rate' , tooltip='Default cell oxygen uptake rate', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='Base/maximum cell speed' , tooltip='Base/maximum cell speed', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='Cell directional persistence time' , tooltip='Cell directional persistence time', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='Strength of leader cells\' cell-cell adhesion' , tooltip='Strength of leader cells\' cell-cell adhesion', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='Strength of leader cells\' cell-cell repulsion' , tooltip='Strength of leader cells\' cell-cell repulsion', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='Leader chemotaxis bias' , tooltip='Leader chemotaxis bias', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='Anisotropy rate of increase' , tooltip='Anisotropy rate of increase', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='Fiber rate of realignment' , tooltip='Fiber rate of realignment', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='Cell ECM density target' , tooltip='Cell ECM density target', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='Strength of follower cells\' cell-cell adhesion' , tooltip='Strength of follower cells\' cell-cell adhesion', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='Strength of follower cells\' cell-cell repulsion' , tooltip='Strength of follower cells\' cell-cell repulsion', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='Follower chemotaxis bias' , tooltip='Follower chemotaxis bias', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='Follower ECM orientation sensitivity' , tooltip='Follower ECM orientation sensitivity', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'
        desc_button19 = Button(description='Minimum ECM density required for cell motility' , tooltip='Minimum ECM density required for cell motility', disabled=True, layout=desc_button_layout) 
        desc_button19.style.button_color = 'lightgreen'
        desc_button20 = Button(description='Maximum ECM density allowing cell motility' , tooltip='Maximum ECM density allowing cell motility', disabled=True, layout=desc_button_layout) 
        desc_button20.style.button_color = 'tan'
        desc_button21 = Button(description='Ideal ECM density cell motility' , tooltip='Ideal ECM density cell motility', disabled=True, layout=desc_button_layout) 
        desc_button21.style.button_color = 'lightgreen'
        desc_button22 = Button(description='Sensitivity to previous direction (hysteresis model only)' , tooltip='Sensitivity to previous direction (hysteresis model only)', disabled=True, layout=desc_button_layout) 
        desc_button22.style.button_color = 'tan'
        desc_button23 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button23.style.button_color = 'lightgreen'
        desc_button24 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button24.style.button_color = 'tan'
        desc_button25 = Button(description='Oxygen decay rate' , tooltip='Oxygen decay rate', disabled=True, layout=desc_button_layout) 
        desc_button25.style.button_color = 'lightgreen'
        desc_button26 = Button(description='Starburst, vertical up, horizontal right, angle, or none' , tooltip='Starburst, vertical up, horizontal right, angle, or none', disabled=True, layout=desc_button_layout) 
        desc_button26.style.button_color = 'tan'
        desc_button27 = Button(description='Angle of chemical field gradient orientation, specified in degrees' , tooltip='Angle of chemical field gradient orientation, specified in degrees', disabled=True, layout=desc_button_layout) 
        desc_button27.style.button_color = 'lightgreen'
        desc_button28 = Button(description='Random, horizontal, vertical, circular, starburst, or split' , tooltip='Random, horizontal, vertical, circular, starburst, or split', disabled=True, layout=desc_button_layout) 
        desc_button28.style.button_color = 'tan'
        desc_button29 = Button(description='Length of ECM unit in x-direction' , tooltip='Length of ECM unit in x-direction', disabled=True, layout=desc_button_layout) 
        desc_button29.style.button_color = 'lightgreen'
        desc_button30 = Button(description='Length of ECM unit in y-direction' , tooltip='Length of ECM unit in y-direction', disabled=True, layout=desc_button_layout) 
        desc_button30.style.button_color = 'tan'
        desc_button31 = Button(description='Length of ECM unit in z-direction' , tooltip='Length of ECM unit in z-direction', disabled=True, layout=desc_button_layout) 
        desc_button31.style.button_color = 'lightgreen'
        desc_button32 = Button(description='follower chemotaxis/no follower hysteresis, follower hysteresis/no follower chemotaxis' , tooltip='follower chemotaxis/no follower hysteresis, follower hysteresis/no follower chemotaxis', disabled=True, layout=desc_button_layout) 
        desc_button32.style.button_color = 'tan'
        desc_button33 = Button(description='ECM remodeling: 1 = finite speed; 0 = instant' , tooltip='ECM remodeling: 1 = finite speed; 0 = instant', disabled=True, layout=desc_button_layout) 
        desc_button33.style.button_color = 'lightgreen'
        desc_button34 = Button(description='Selects if chemotaxtic bias on followers is coupled exactly to ECM anisotropy or not: 1 = not coupled; 0 = coupled' , tooltip='Selects if chemotaxtic bias on followers is coupled exactly to ECM anisotropy or not: 1 = not coupled; 0 = coupled', disabled=True, layout=desc_button_layout) 
        desc_button34.style.button_color = 'tan'
        desc_button35 = Button(description='Specifies ECM reorientation model: ecm_update_from_cell_motility_vector or ecm_update_from_cell_velocity_vector' , tooltip='Specifies ECM reorientation model: ecm_update_from_cell_motility_vector or ecm_update_from_cell_velocity_vector', disabled=True, layout=desc_button_layout) 
        desc_button35.style.button_color = 'lightgreen'
        desc_button36 = Button(description='Normalize follower motility vector' , tooltip='Normalize follower motility vector', disabled=True, layout=desc_button_layout) 
        desc_button36.style.button_color = 'tan'
        desc_button37 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button37.style.button_color = 'lightgreen'
        desc_button38 = Button(description='Use to freeze chemical and ECM fields' , tooltip='Use to freeze chemical and ECM fields', disabled=True, layout=desc_button_layout) 
        desc_button38.style.button_color = 'tan'
        desc_button39 = Button(description='Sets parameters for testing: 1 for testing, 0 for typical simulation' , tooltip='Sets parameters for testing: 1 for testing, 0 for typical simulation', disabled=True, layout=desc_button_layout) 
        desc_button39.style.button_color = 'lightgreen'
        desc_button40 = Button(description='Testing set up: 1 for cell march, 0 for typical simulation' , tooltip='Testing set up: 1 for cell march, 0 for typical simulation', disabled=True, layout=desc_button_layout) 
        desc_button40.style.button_color = 'tan'
        desc_button41 = Button(description='Specifies pattern of line overlay: none, horizontal lines, vertical lines, or concentric circles' , tooltip='Specifies pattern of line overlay: none, horizontal lines, vertical lines, or concentric circles', disabled=True, layout=desc_button_layout) 
        desc_button41.style.button_color = 'lightgreen'
        desc_button42 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button42.style.button_color = 'tan'

        row1 = [param_name1, self.initial_anisotropy, units_button1, desc_button1] 
        row2 = [param_name2, self.initial_ECM_density, units_button2, desc_button2] 
        row3 = [param_name3, self.cell_setup, units_button3, desc_button3] 
        row4 = [param_name4, self.tumor_radius, units_button4, desc_button4] 
        row5 = [param_name5, self.initial_leader_cell_fraction, units_button5, desc_button5] 
        row6 = [param_name6, self.oxygen_uptake, units_button6, desc_button6] 
        row7 = [param_name7, self.default_cell_speed, units_button7, desc_button7] 
        row8 = [param_name8, self.default_persistence_time, units_button8, desc_button8] 
        row9 = [param_name9, self.leader_adhesion, units_button9, desc_button9] 
        row10 = [param_name10, self.leader_repulsion, units_button10, desc_button10] 
        row11 = [param_name11, self.oxygen_migration_bias_for_leaders, units_button11, desc_button11] 
        row12 = [param_name12, self.anisotropy_increase_rate, units_button12, desc_button12] 
        row13 = [param_name13, self.fiber_realignment_rate, units_button13, desc_button13] 
        row14 = [param_name14, self.default_ECM_density_target, units_button14, desc_button14] 
        row15 = [param_name15, self.follower_adhesion, units_button15, desc_button15] 
        row16 = [param_name16, self.follower_repulsion, units_button16, desc_button16] 
        row17 = [param_name17, self.default_chemotaxis_bias, units_button17, desc_button17] 
        row18 = [param_name18, self.default_ECM_sensitivity, units_button18, desc_button18] 
        row19 = [param_name19, self.rho_L, units_button19, desc_button19] 
        row20 = [param_name20, self.rho_H, units_button20, desc_button20] 
        row21 = [param_name21, self.rho_I, units_button21, desc_button21] 
        row22 = [param_name22, self.default_hysteresis_bias, units_button22, desc_button22] 
        row23 = [param_name23, self.leader_motility_mode, units_button23, desc_button23] 
        row24 = [param_name24, self.follower_motility_mode, units_button24, desc_button24] 
        row25 = [param_name25, self.chemotactic_substrate_decay_rate, units_button25, desc_button25] 
        row26 = [param_name26, self.chemical_field_setup, units_button26, desc_button26] 
        row27 = [param_name27, self.angle_of_chemical_field_gradient, units_button27, desc_button27] 
        row28 = [param_name28, self.ECM_orientation_setup, units_button28, desc_button28] 
        row29 = [param_name29, self.ECM_dx, units_button29, desc_button29] 
        row30 = [param_name30, self.ECM_dy, units_button30, desc_button30] 
        row31 = [param_name31, self.ECM_dz, units_button31, desc_button31] 
        row32 = [param_name32, self.cell_motility_ECM_interaction_model_selector, units_button32, desc_button32] 
        row33 = [param_name33, self.discrete_ECM_remodeling, units_button33, desc_button33] 
        row34 = [param_name34, self.link_anisotropy_and_bias, units_button34, desc_button34] 
        row35 = [param_name35, self.ecm_update_model, units_button35, desc_button35] 
        row36 = [param_name36, self.normalize_ECM_influenced_motility_vector, units_button36, desc_button36] 
        row37 = [param_name37, self.duration_of_uE_conditioning, units_button37, desc_button37] 
        row38 = [param_name38, self.freeze_uE_profile, units_button38, desc_button38] 
        row39 = [param_name39, self.unit_test_setup, units_button39, desc_button39] 
        row40 = [param_name40, self.march_unit_test_setup, units_button40, desc_button40] 
        row41 = [param_name41, self.visual_guideline_pattern, units_button41, desc_button41] 
        row42 = [param_name42, self.enable_ecm_outputs, units_button42, desc_button42] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)
        box15 = Box(children=row15, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)
        box19 = Box(children=row19, layout=box_layout)
        box20 = Box(children=row20, layout=box_layout)
        box21 = Box(children=row21, layout=box_layout)
        box22 = Box(children=row22, layout=box_layout)
        box23 = Box(children=row23, layout=box_layout)
        box24 = Box(children=row24, layout=box_layout)
        box25 = Box(children=row25, layout=box_layout)
        box26 = Box(children=row26, layout=box_layout)
        box27 = Box(children=row27, layout=box_layout)
        box28 = Box(children=row28, layout=box_layout)
        box29 = Box(children=row29, layout=box_layout)
        box30 = Box(children=row30, layout=box_layout)
        box31 = Box(children=row31, layout=box_layout)
        box32 = Box(children=row32, layout=box_layout)
        box33 = Box(children=row33, layout=box_layout)
        box34 = Box(children=row34, layout=box_layout)
        box35 = Box(children=row35, layout=box_layout)
        box36 = Box(children=row36, layout=box_layout)
        box37 = Box(children=row37, layout=box_layout)
        box38 = Box(children=row38, layout=box_layout)
        box39 = Box(children=row39, layout=box_layout)
        box40 = Box(children=row40, layout=box_layout)
        box41 = Box(children=row41, layout=box_layout)
        box42 = Box(children=row42, layout=box_layout)

        self.tab = VBox([
          box1,
          box2,
          box3,
          box4,
          box5,
          box6,
          box7,
          box8,
          box9,
          box10,
          box11,
          box12,
          box13,
          box14,
          box15,
          box16,
          box17,
          box18,
          box19,
          box20,
          box21,
          box22,
          box23,
          box24,
          box25,
          box26,
          box27,
          box28,
          box29,
          box30,
          box31,
          box32,
          box33,
          box34,
          box35,
          box36,
          box37,
          box38,
          box39,
          box40,
          box41,
          box42,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.initial_anisotropy.value = float(uep.find('.//initial_anisotropy').text)
        self.initial_ECM_density.value = float(uep.find('.//initial_ECM_density').text)
        self.cell_setup.value = (uep.find('.//cell_setup').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.initial_leader_cell_fraction.value = float(uep.find('.//initial_leader_cell_fraction').text)
        self.oxygen_uptake.value = float(uep.find('.//oxygen_uptake').text)
        self.default_cell_speed.value = float(uep.find('.//default_cell_speed').text)
        self.default_persistence_time.value = float(uep.find('.//default_persistence_time').text)
        self.leader_adhesion.value = float(uep.find('.//leader_adhesion').text)
        self.leader_repulsion.value = float(uep.find('.//leader_repulsion').text)
        self.oxygen_migration_bias_for_leaders.value = float(uep.find('.//oxygen_migration_bias_for_leaders').text)
        self.anisotropy_increase_rate.value = float(uep.find('.//anisotropy_increase_rate').text)
        self.fiber_realignment_rate.value = float(uep.find('.//fiber_realignment_rate').text)
        self.default_ECM_density_target.value = float(uep.find('.//default_ECM_density_target').text)
        self.follower_adhesion.value = float(uep.find('.//follower_adhesion').text)
        self.follower_repulsion.value = float(uep.find('.//follower_repulsion').text)
        self.default_chemotaxis_bias.value = float(uep.find('.//default_chemotaxis_bias').text)
        self.default_ECM_sensitivity.value = float(uep.find('.//default_ECM_sensitivity').text)
        self.rho_L.value = float(uep.find('.//rho_L').text)
        self.rho_H.value = float(uep.find('.//rho_H').text)
        self.rho_I.value = float(uep.find('.//rho_I').text)
        self.default_hysteresis_bias.value = float(uep.find('.//default_hysteresis_bias').text)
        self.leader_motility_mode.value = ('true' == (uep.find('.//leader_motility_mode').text.lower()) )
        self.follower_motility_mode.value = ('true' == (uep.find('.//follower_motility_mode').text.lower()) )
        self.chemotactic_substrate_decay_rate.value = float(uep.find('.//chemotactic_substrate_decay_rate').text)
        self.chemical_field_setup.value = (uep.find('.//chemical_field_setup').text)
        self.angle_of_chemical_field_gradient.value = float(uep.find('.//angle_of_chemical_field_gradient').text)
        self.ECM_orientation_setup.value = (uep.find('.//ECM_orientation_setup').text)
        self.ECM_dx.value = float(uep.find('.//ECM_dx').text)
        self.ECM_dy.value = float(uep.find('.//ECM_dy').text)
        self.ECM_dz.value = float(uep.find('.//ECM_dz').text)
        self.cell_motility_ECM_interaction_model_selector.value = (uep.find('.//cell_motility_ECM_interaction_model_selector').text)
        self.discrete_ECM_remodeling.value = int(uep.find('.//discrete_ECM_remodeling').text)
        self.link_anisotropy_and_bias.value = int(uep.find('.//link_anisotropy_and_bias').text)
        self.ecm_update_model.value = (uep.find('.//ecm_update_model').text)
        self.normalize_ECM_influenced_motility_vector.value = ('true' == (uep.find('.//normalize_ECM_influenced_motility_vector').text.lower()) )
        self.duration_of_uE_conditioning.value = float(uep.find('.//duration_of_uE_conditioning').text)
        self.freeze_uE_profile.value = ('true' == (uep.find('.//freeze_uE_profile').text.lower()) )
        self.unit_test_setup.value = int(uep.find('.//unit_test_setup').text)
        self.march_unit_test_setup.value = int(uep.find('.//march_unit_test_setup').text)
        self.visual_guideline_pattern.value = (uep.find('.//visual_guideline_pattern').text)
        self.enable_ecm_outputs.value = ('true' == (uep.find('.//enable_ecm_outputs').text.lower()) )


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//initial_anisotropy').text = str(self.initial_anisotropy.value)
        uep.find('.//initial_ECM_density').text = str(self.initial_ECM_density.value)
        uep.find('.//cell_setup').text = str(self.cell_setup.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//initial_leader_cell_fraction').text = str(self.initial_leader_cell_fraction.value)
        uep.find('.//oxygen_uptake').text = str(self.oxygen_uptake.value)
        uep.find('.//default_cell_speed').text = str(self.default_cell_speed.value)
        uep.find('.//default_persistence_time').text = str(self.default_persistence_time.value)
        uep.find('.//leader_adhesion').text = str(self.leader_adhesion.value)
        uep.find('.//leader_repulsion').text = str(self.leader_repulsion.value)
        uep.find('.//oxygen_migration_bias_for_leaders').text = str(self.oxygen_migration_bias_for_leaders.value)
        uep.find('.//anisotropy_increase_rate').text = str(self.anisotropy_increase_rate.value)
        uep.find('.//fiber_realignment_rate').text = str(self.fiber_realignment_rate.value)
        uep.find('.//default_ECM_density_target').text = str(self.default_ECM_density_target.value)
        uep.find('.//follower_adhesion').text = str(self.follower_adhesion.value)
        uep.find('.//follower_repulsion').text = str(self.follower_repulsion.value)
        uep.find('.//default_chemotaxis_bias').text = str(self.default_chemotaxis_bias.value)
        uep.find('.//default_ECM_sensitivity').text = str(self.default_ECM_sensitivity.value)
        uep.find('.//rho_L').text = str(self.rho_L.value)
        uep.find('.//rho_H').text = str(self.rho_H.value)
        uep.find('.//rho_I').text = str(self.rho_I.value)
        uep.find('.//default_hysteresis_bias').text = str(self.default_hysteresis_bias.value)
        uep.find('.//leader_motility_mode').text = str(self.leader_motility_mode.value)
        uep.find('.//follower_motility_mode').text = str(self.follower_motility_mode.value)
        uep.find('.//chemotactic_substrate_decay_rate').text = str(self.chemotactic_substrate_decay_rate.value)
        uep.find('.//chemical_field_setup').text = str(self.chemical_field_setup.value)
        uep.find('.//angle_of_chemical_field_gradient').text = str(self.angle_of_chemical_field_gradient.value)
        uep.find('.//ECM_orientation_setup').text = str(self.ECM_orientation_setup.value)
        uep.find('.//ECM_dx').text = str(self.ECM_dx.value)
        uep.find('.//ECM_dy').text = str(self.ECM_dy.value)
        uep.find('.//ECM_dz').text = str(self.ECM_dz.value)
        uep.find('.//cell_motility_ECM_interaction_model_selector').text = str(self.cell_motility_ECM_interaction_model_selector.value)
        uep.find('.//discrete_ECM_remodeling').text = str(self.discrete_ECM_remodeling.value)
        uep.find('.//link_anisotropy_and_bias').text = str(self.link_anisotropy_and_bias.value)
        uep.find('.//ecm_update_model').text = str(self.ecm_update_model.value)
        uep.find('.//normalize_ECM_influenced_motility_vector').text = str(self.normalize_ECM_influenced_motility_vector.value)
        uep.find('.//duration_of_uE_conditioning').text = str(self.duration_of_uE_conditioning.value)
        uep.find('.//freeze_uE_profile').text = str(self.freeze_uE_profile.value)
        uep.find('.//unit_test_setup').text = str(self.unit_test_setup.value)
        uep.find('.//march_unit_test_setup').text = str(self.march_unit_test_setup.value)
        uep.find('.//visual_guideline_pattern').text = str(self.visual_guideline_pattern.value)
        uep.find('.//enable_ecm_outputs').text = str(self.enable_ecm_outputs.value)
