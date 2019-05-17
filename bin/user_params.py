 
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
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}

        param_name1 = Button(description='Model_Initialization', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.Model_Initialization = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name2 = Button(description='ECM_initialization_parameters', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.ECM_initialization_parameters = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name3 = Button(description='initial_anisotropy', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.initial_anisotropy = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name4 = Button(description='initial_ECM_density', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.initial_ECM_density = FloatText(
          value=0.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name5 = Button(description='Lesion_intialization', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.Lesion_intialization = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name6 = Button(description='tumor_radius', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.tumor_radius = FloatText(
          value=150,
          step=10,
          style=style, layout=widget_layout)

        param_name7 = Button(description='initial_leader_cell_fraction', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.initial_leader_cell_fraction = FloatText(
          value=0.0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name8 = Button(description='Cell_properties', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.Cell_properties = FloatText(
          value=0,
          step=0.01,
          style=style, layout=widget_layout)

        param_name9 = Button(description='leader_adhesion', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.leader_adhesion = FloatText(
          value=6.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name10 = Button(description='leader_repulsion', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.leader_repulsion = FloatText(
          value=25,
          step=1,
          style=style, layout=widget_layout)

        param_name11 = Button(description='follower_adhesion', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'lightgreen'

        self.follower_adhesion = FloatText(
          value=6.5,
          step=0.1,
          style=style, layout=widget_layout)

        param_name12 = Button(description='follower_repulsion', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'tan'

        self.follower_repulsion = FloatText(
          value=25,
          step=1,
          style=style, layout=widget_layout)

        param_name13 = Button(description='default_cell_speed', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'lightgreen'

        self.default_cell_speed = FloatText(
          value=0.3,
          step=0.01,
          style=style, layout=widget_layout)

        param_name14 = Button(description='default_persistence_time', disabled=True, layout=name_button_layout)
        param_name14.style.button_color = 'tan'

        self.default_persistence_time = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        param_name15 = Button(description='default_ECM_sensitivity', disabled=True, layout=name_button_layout)
        param_name15.style.button_color = 'lightgreen'

        self.default_ECM_sensitivity = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        param_name16 = Button(description='oxygen_migration_bias_for_leaders', disabled=True, layout=name_button_layout)
        param_name16.style.button_color = 'tan'

        self.oxygen_migration_bias_for_leaders = FloatText(
          value=0.95,
          step=0.1,
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='microns', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='microns/minute', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='minutes', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'
        units_button15 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'lightgreen'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'tan'

        desc_button1 = Button(description='This is a spacer', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button2 = Button(description='ECM_initialization_parameters', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='Initial ECM anisotropy', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='Initial ECM density', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='Lesion_intialization', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='Initial cell mass radius', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='Average percentage of leaders initialized', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='Cell_properties', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='Strength of leader cells\' cell-cell adhesion', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='Strength of leader cells\' cell-cell repulsion', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='Strength of follower cells\' cell-cell adhesion', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='Strength of follower cells\' cell-cell repulsion', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='Base/maximum cell speed', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='Cell directional persistence time', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'
        desc_button15 = Button(description='Cell sensitivity to ECM orientation for ECM following type cells', disabled=True, layout=desc_button_layout) 
        desc_button15.style.button_color = 'lightgreen'
        desc_button16 = Button(description='Chemotaxis bias for non-ECM influenced cell types', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'

        row1 = [param_name1, self.Model_Initialization, units_button1, desc_button1] 
        row2 = [param_name2, self.ECM_initialization_parameters, units_button2, desc_button2] 
        row3 = [param_name3, self.initial_anisotropy, units_button3, desc_button3] 
        row4 = [param_name4, self.initial_ECM_density, units_button4, desc_button4] 
        row5 = [param_name5, self.Lesion_intialization, units_button5, desc_button5] 
        row6 = [param_name6, self.tumor_radius, units_button6, desc_button6] 
        row7 = [param_name7, self.initial_leader_cell_fraction, units_button7, desc_button7] 
        row8 = [param_name8, self.Cell_properties, units_button8, desc_button8] 
        row9 = [param_name9, self.leader_adhesion, units_button9, desc_button9] 
        row10 = [param_name10, self.leader_repulsion, units_button10, desc_button10] 
        row11 = [param_name11, self.follower_adhesion, units_button11, desc_button11] 
        row12 = [param_name12, self.follower_repulsion, units_button12, desc_button12] 
        row13 = [param_name13, self.default_cell_speed, units_button13, desc_button13] 
        row14 = [param_name14, self.default_persistence_time, units_button14, desc_button14] 
        row15 = [param_name15, self.default_ECM_sensitivity, units_button15, desc_button15] 
        row16 = [param_name16, self.oxygen_migration_bias_for_leaders, units_button16, desc_button16] 

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
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML
        self.Model_Initialization.value = float(uep.find('.//Model_Initialization').text)
        self.ECM_initialization_parameters.value = float(uep.find('.//ECM_initialization_parameters').text)
        self.initial_anisotropy.value = float(uep.find('.//initial_anisotropy').text)
        self.initial_ECM_density.value = float(uep.find('.//initial_ECM_density').text)
        self.Lesion_intialization.value = float(uep.find('.//Lesion_intialization').text)
        self.tumor_radius.value = float(uep.find('.//tumor_radius').text)
        self.initial_leader_cell_fraction.value = float(uep.find('.//initial_leader_cell_fraction').text)
        self.Cell_properties.value = float(uep.find('.//Cell_properties').text)
        self.leader_adhesion.value = float(uep.find('.//leader_adhesion').text)
        self.leader_repulsion.value = float(uep.find('.//leader_repulsion').text)
        self.follower_adhesion.value = float(uep.find('.//follower_adhesion').text)
        self.follower_repulsion.value = float(uep.find('.//follower_repulsion').text)
        self.default_cell_speed.value = float(uep.find('.//default_cell_speed').text)
        self.default_persistence_time.value = float(uep.find('.//default_persistence_time').text)
        self.default_ECM_sensitivity.value = float(uep.find('.//default_ECM_sensitivity').text)
        self.oxygen_migration_bias_for_leaders.value = float(uep.find('.//oxygen_migration_bias_for_leaders').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//user_parameters')  # find unique entry point into XML 
        uep.find('.//Model_Initialization').text = str(self.Model_Initialization.value)
        uep.find('.//ECM_initialization_parameters').text = str(self.ECM_initialization_parameters.value)
        uep.find('.//initial_anisotropy').text = str(self.initial_anisotropy.value)
        uep.find('.//initial_ECM_density').text = str(self.initial_ECM_density.value)
        uep.find('.//Lesion_intialization').text = str(self.Lesion_intialization.value)
        uep.find('.//tumor_radius').text = str(self.tumor_radius.value)
        uep.find('.//initial_leader_cell_fraction').text = str(self.initial_leader_cell_fraction.value)
        uep.find('.//Cell_properties').text = str(self.Cell_properties.value)
        uep.find('.//leader_adhesion').text = str(self.leader_adhesion.value)
        uep.find('.//leader_repulsion').text = str(self.leader_repulsion.value)
        uep.find('.//follower_adhesion').text = str(self.follower_adhesion.value)
        uep.find('.//follower_repulsion').text = str(self.follower_repulsion.value)
        uep.find('.//default_cell_speed').text = str(self.default_cell_speed.value)
        uep.find('.//default_persistence_time').text = str(self.default_persistence_time.value)
        uep.find('.//default_ECM_sensitivity').text = str(self.default_ECM_sensitivity.value)
        uep.find('.//oxygen_migration_bias_for_leaders').text = str(self.oxygen_migration_bias_for_leaders.value)
