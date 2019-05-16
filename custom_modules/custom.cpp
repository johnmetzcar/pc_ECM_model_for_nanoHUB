/*
###############################################################################
# If you use PhysiCell in your project, please cite PhysiCell and the version #
# number, such as below:                                                      #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1].    #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# See VERSION.txt or call get_PhysiCell_version() to get the current version  #
#     x.y.z. Call display_citations() to get detailed information on all cite-#
#     able software used in your PhysiCell application.                       #
#                                                                             #
# Because PhysiCell extensively uses BioFVM, we suggest you also cite BioFVM  #
#     as below:                                                               #
#                                                                             #
# We implemented and solved the model using PhysiCell (Version x.y.z) [1],    #
# with BioFVM [2] to solve the transport equations.                           #
#                                                                             #
# [1] A Ghaffarizadeh, R Heiland, SH Friedman, SM Mumenthaler, and P Macklin, #
#     PhysiCell: an Open Source Physics-Based Cell Simulator for Multicellu-  #
#     lar Systems, PLoS Comput. Biol. 14(2): e1005991, 2018                   #
#     DOI: 10.1371/journal.pcbi.1005991                                       #
#                                                                             #
# [2] A Ghaffarizadeh, SH Friedman, and P Macklin, BioFVM: an efficient para- #
#     llelized diffusive transport solver for 3-D biological simulations,     #
#     Bioinformatics 32(8): 1256-8, 2016. DOI: 10.1093/bioinformatics/btv730  #
#                                                                             #
###############################################################################
#                                                                             #
# BSD 3-Clause License (see https://opensource.org/licenses/BSD-3-Clause)     #
#                                                                             #
# Copyright (c) 2015-2018, Paul Macklin and the PhysiCell Project             #
# All rights reserved.                                                        #
#                                                                             #
# Redistribution and use in source and binary forms, with or without          #
# modification, are permitted provided that the following conditions are met: #
#                                                                             #
# 1. Redistributions of source code must retain the above copyright notice,   #
# this list of conditions and the following disclaimer.                       #
#                                                                             #
# 2. Redistributions in binary form must reproduce the above copyright        #
# notice, this list of conditions and the following disclaimer in the         #
# documentation and/or other materials provided with the distribution.        #
#                                                                             #
# 3. Neither the name of the copyright holder nor the names of its            #
# contributors may be used to endorse or promote products derived from this   #
# software without specific prior written permission.                         #
#                                                                             #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE   #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE  #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE   #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF        #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS    #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN     #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)     #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE  #
# POSSIBILITY OF SUCH DAMAGE.                                                 #
#                                                                             #
###############################################################################
*/

#include "./custom.h"

// declare cell definitions here 

Cell_Definition motile_cell; 

std::vector< std::vector<double> > ECM_fiber_alignment; 

void create_cell_types( void )
{
	SeedRandom( 0.595959);//parameters.ints("random_seed") ); // or specify a seed here 

	// housekeeping 
	initialize_default_cell_definition();
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment ); 
	
	// Name the default cell type 
	cell_defaults.type = 0; 
	cell_defaults.name = "cell"; 
	
	// set default cell cycle model 
	cell_defaults.functions.cycle_model = live; // let's keep it simple 
	
	// set default_cell_functions; 
	cell_defaults.functions.update_phenotype = NULL; // no need for fancy stuff here 
	cell_defaults.functions.update_migration_bias = ECM_motility_aligned; 
	
	// needed for a 2-D simulation: 
	cell_defaults.functions.set_orientation = up_orientation; 
	cell_defaults.phenotype.geometry.polarity = 1.0;
	cell_defaults.phenotype.motility.restrict_to_2D = true; 
	
	// make sure the defaults are self-consistent. 
	cell_defaults.phenotype.secretion.sync_to_microenvironment( &microenvironment );
	cell_defaults.phenotype.sync_to_functions( cell_defaults.functions ); 

	// first find indices for a few key variables. 
	int apoptosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Apoptosis" );
	int necrosis_model_index = cell_defaults.phenotype.death.find_death_model_index( "Necrosis" );
	int oxygen_substrate_index = microenvironment.find_density_index( "oxygen" ); 
	int nCycle_start = live.find_phase_index( PhysiCell_constants::live );
	int nCycle_end = live.find_phase_index( PhysiCell_constants::live );

	// set oxygen uptake / secretion parameters for the default cell type 
	cell_defaults.phenotype.secretion.uptake_rates[oxygen_substrate_index] = 10; 
	cell_defaults.phenotype.secretion.secretion_rates[oxygen_substrate_index] = 0; 
	cell_defaults.phenotype.secretion.saturation_densities[oxygen_substrate_index] = 38; 
	
	// add custom data here, if any 

	/*************************************Start of custom code here***********************************************/

	/**First thing we'll do is allow cells to "uptake" the ECM to simulate decay**/

	int ecm_index = microenvironment.find_density_index("ECM");

	/***********************We'll need to play around with this, but for now just set it to the same uptake rate as O2*********************/
	cell_defaults.phenotype.secretion.uptake_rates[ecm_index] = parameters.doubles("ecm_uptake_rate");


	cell_defaults.custom_data.add_variable( "max speed", "micron/min" , 
	parameters.doubles( "max_migration_speed") ); 
	
	// enable motility 
	cell_defaults.phenotype.motility.is_motile = true; 
	cell_defaults.phenotype.motility.persistence_time = 15.0; //parameters.doubles( "migration_persistence_time" ); // 15.0; 
	cell_defaults.phenotype.motility.migration_speed = 0.25; //parameters.doubles( "max_migration_speed" ); // 0.25 micron/minute 
	cell_defaults.phenotype.motility.migration_bias = 0.0;// completely random 
	
	// Set birth and death rates to zero 
	cell_defaults.phenotype.death.rates[apoptosis_model_index] = 0.0; 
	cell_defaults.phenotype.death.rates[necrosis_model_index] = 0.0; 
	cell_defaults.phenotype.cycle.data.transition_rate(nCycle_start,nCycle_end) = 0.0; 
	 
	return; 
}

void setup_microenvironment( void )
{
	// make sure to override and go back to 2D 
	if( default_microenvironment_options.simulate_2D == false )
	{
		std::cout << "Warning: overriding XML config option and setting to 2D!" << std::endl; 
		default_microenvironment_options.simulate_2D = true; 
	}
	
	microenvironment.add_density( "ECM", "dimensionless", 0.0 , 0.0 ); 
	microenvironment.add_density( "ECM anisotropy" , "dimensionless" , 0.0 , 0.0 ); 
	
	// calculate gradients, just in case 
	default_microenvironment_options.calculate_gradients = true; 
	
	// set Dirichlet conditions 
	default_microenvironment_options.outer_Dirichlet_conditions = true;
	
	// if there are more substrates, resize accordingly 
	std::vector<double> bc_vector = { 38.0 , 0.5 , 1 };  // 5% o2 , half max ECM , isotropic  
	default_microenvironment_options.Dirichlet_condition_vector = bc_vector;
	
	// initialize BioFVM 
	initialize_microenvironment(); 	
	
	// set up ECM profile
	int nECM = microenvironment.find_density_index( "ECM" ); 
	int nECM_A = microenvironment.find_density_index( "ECM anisotropy" ); 
	/*for( int n = 0; n < microenvironment.mesh.voxels.size() ; n++ )
	{
		std::vector<double> position = microenvironment.mesh.voxels[n].center; 
		if( fabs( position[0] ) > 200 || fabs( position[1] ) > 200 )
		{
			microenvironment(n)[nECM] = 0.0; 
			microenvironment(n)[nECM_A] = 1.0; 
		}
	}*/
	
	// set up ECM alignment 
	std::vector<double> fiber_direction = { 1.0 , 0.0, 0.0 }; 
	ECM_fiber_alignment.resize( microenvironment.mesh.voxels.size() , fiber_direction );  
	
	for( int n = 0; n < microenvironment.mesh.voxels.size() ; n++ )
	{
		std::vector<double> position = microenvironment.mesh.voxels[n].center; 
		normalize( position ); 
		ECM_fiber_alignment[n] =  { position[0],position[1],0};
		//Paul's initial position { -position[1],position[0],0}; // position; 
	}
	
	return; 
}

void setup_tissue( void )
{
	/*******************************************Random initialization****************************************/
	/*Cell* pC;
	
	for( int n = 0 ; n < 200 ; n++ )
	{
		pC = create_cell(); 
		pC->assign_position( -450 + 900*UniformRandom() , -450 + 900*UniformRandom() , 0.0 );
	}*/

	/******************************************2D Spheroid initialization***************************************/

	//Get tumor radius from XML parameters
	double tumor_radius = parameters.doubles("tumor_radius");
	double cell_radius = cell_defaults.phenotype.geometry.radius;
    //double relative_maximum_adhesion_distance = cell_defaults.phenotype.mechanics.relative_maximum_adhesion_distance;
    //double sqrt_adhesion_to_repulsion_ratio = sqrt(parameters.doubles("follower_adhesion")/parameters.doubles("follower_repulsion"));
    
    double cell_spacing = 0.95 * 2.0 * cell_radius;//(1 - sqrt_adhesion_to_repulsion_ratio);
    //cell_spacing /= (0.5 * 1/cell_radius - 0.5 * sqrt_adhesion_to_repulsion_ratio/(relative_maximum_adhesion_distance * cell_radius));
	
    std::cout<<2*cell_radius<<std::endl;
    std::cout<<cell_spacing<<std::endl;
    std::cout<<cell_spacing/(2*cell_radius)<<std::endl;
    
	Cell* pCell = NULL; 
	
	double x = 0.0;
	double x_outer = tumor_radius; 
	double y = 0.0;
	
	//double leader_cell_fraction = 0.2;
	
	int n = 0; 
	while( y < tumor_radius )
	{
		x = 0.0; 
		if( n % 2 == 1 )
		{ x = 0.5*cell_spacing; }
		x_outer = sqrt( tumor_radius*tumor_radius - y*y ); 
		
		while( x < x_outer )
		{
			pCell = create_cell();
				
			pCell->assign_position( x , y , 0.0 );

			
			if( fabs( y ) > 0.01 )
			{
				pCell = create_cell();
				pCell->assign_position( x , -y , 0.0 );
			}
			
			if( fabs( x ) > 0.01 )
			{ 
				pCell = create_cell();
				pCell->assign_position( -x , y , 0.0 );
				
				if( fabs( y ) > 0.01 )
				{
					pCell = create_cell();
					pCell->assign_position( -x , -y , 0.0 );
				}
			}
			x += cell_spacing; 
			
		}
		
		y += cell_spacing * sqrt(3.0)/2.0; 
		n++; 
	}
		

	/******************************************3D Spheroid initialization***************************************/

	/*To come later*/

	return; 
}

std::vector<std::string> my_coloring_function( Cell* pCell )
{
	// start with flow cytometry coloring 
	
	std::vector<std::string> output( 4 , "red" ); 
	
	return output; 
}

void ECM_motility( Cell* pCell, Phenotype& phenotype, double dt )
{
	// find location of variables 
	static int nECM = microenvironment.find_density_index( "ECM" ); 
	static int nMaxSpeed = pCell->custom_data.find_variable_index( "max speed" ); 
	
	// sample ECM 
	double ECM = pCell->nearest_density_vector()[nECM]; 
	std::cout << std::endl << "Density = " << ECM << std::endl;
	phenotype.motility.migration_speed = (pCell->custom_data[nMaxSpeed]) * ECM * (1-ECM) *4.0; 
	
	return; 
}

double dot_product( const std::vector<double>& v , const std::vector<double>& w )
{
 double out = 0.0; 
 for( unsigned int i=0 ; i < v.size() ; i++ )
 { out += ( v[i] * w[i] ); }
 return out; 
}

void ECM_motility_aligned( Cell* pCell, Phenotype& phenotype, double dt )
{
	// find location of variables 
	static int nECM = microenvironment.find_density_index( "ECM" ); 
	static int nMaxSpeed = pCell->custom_data.find_variable_index( "max speed" ); 
	static int nECM_A = microenvironment.find_density_index( "ECM anisotropy" ); 
	
	// sample ECM 
	double ECM = pCell->nearest_density_vector()[nECM]; 
	double a = pCell->nearest_density_vector()[nECM_A]; 
	
	int n = pCell->get_current_voxel_index();

	
	double angle = UniformRandom() * 6.283185307179586;
	std::vector<double> d_mot = { cos(angle) , sin(angle) , 0.0 }; 
	
	// fiber direction
	std::vector<double> f = ECM_fiber_alignment[n]; 
	
	// part of d_mot that is perpendicular to f; 
	std::vector<double> d_perp = d_mot - dot_product(d_mot,f)*f; 
	normalize( d_perp ); 
	
	double c_1 = dot_product( d_mot , d_perp ); 
	double c_2 = dot_product( d_mot, f ); 
	
	double sensitivity = 1.0; 
	double theta = a*sensitivity; 

	std::vector<double> new_migration_bias_direction = (1.0-theta)*c_1*d_perp + c_2*f;
	normalize( new_migration_bias_direction ); 

	/****************************************Add in influence of chemotaxis here****************************************/
	//No clue if this next part is right. I just structured it off of the above code for finding new migration_bias_direction with
	//random influence + ECM influence.

	static int o2_index = microenvironment.find_density_index( "oxygen" ); 
	std::vector<double> chemotaxis_grad = pCell->nearest_gradient(o2_index);
	normalize(chemotaxis_grad);

	//part of new_migration_bias_direction perpendicular to O2 gradient 
	std::vector<double> c_perp = new_migration_bias_direction - dot_product(new_migration_bias_direction,chemotaxis_grad)*chemotaxis_grad;
	normalize( c_perp );

	double c_3 = dot_product( new_migration_bias_direction , c_perp ); 
	double c_4 = dot_product( new_migration_bias_direction, chemotaxis_grad ); 
	
	double chemotaxis_sensitivity = 0.5;

	phenotype.motility.migration_bias_direction = (1.0 - chemotaxis_sensitivity)*c_3*c_perp + c_4*chemotaxis_grad;
	normalize( phenotype.motility.migration_bias_direction ); 

	phenotype.motility.migration_bias = parameters.doubles( "cell_bias" );

	phenotype.motility.migration_speed = (pCell->custom_data[nMaxSpeed]) * ECM * (1-ECM) * 4.0; 
	return; 
}

void ECM_motility_aligned_faster( Cell* pCell, Phenotype& phenotype, double dt )
{
	// find location of variables 
	static int nECM = microenvironment.find_density_index( "ECM" ); 
	static int nMaxSpeed = pCell->custom_data.find_variable_index( "max speed" ); 
	static int nECM_A = microenvironment.find_density_index( "ECM anisotropy" ); 
	
	// sample ECM 
	double ECM = pCell->nearest_density_vector()[nECM]; 
	double a = pCell->nearest_density_vector()[nECM_A]; 
	
	int n = pCell->get_current_voxel_index();

	
	double angle = UniformRandom() * 6.283185307179586;
	std::vector<double> d_mot = { cos(angle) , sin(angle) , 0.0 }; 

	std::vector<double>* pDmot = &( phenotype.motility.migration_bias_direction ); 
	std::vector<double>* pF = &( ECM_fiber_alignment[n] ); 
	
	// part of d_mot that is perpendicular to f; 
	double c2 = dot_product( *pDmot , *pF ); 

	std::vector<double> d_perp = *pF;
	d_perp *= c2; // (dMot.f)*f
	d_perp *= -1; // -(dMot.f)*f
	d_perp += *pDmot; // d_mot - dot(d_mot, f)*f; 
	normalize( d_perp ); 
	
	double c1 = dot_product( *pDmot , d_perp ); 
	
	double sensitivity = 1.0; 
	double theta = a*sensitivity; 
	
	*pDmot = d_perp; 
	*pDmot *= c2; 
	c1 *= (1-theta); // c1*(1-theta) 
	axpy( pDmot , c1 , (d_perp) ); 
	
	
	normalize( *pDmot ); 
	phenotype.motility.migration_bias = 1.0; 

	phenotype.motility.migration_speed = pCell->custom_data[nMaxSpeed]*ECM*(1-ECM)*4.0; 
	return; 
}


void write_ECM_Data_matlab( std::string filename )

{
	static int nECM = microenvironment.find_density_index( "ECM" );
	
	double density = 0;

    int number_of_data_entries = microenvironment.number_of_voxels();
	
    int size_of_each_datum = 4;

    FILE* fp = write_matlab_header( size_of_each_datum, number_of_data_entries,  filename, "ECM_Data" );  // Note - the size of datum needs to correspond exaectly to the lines of output or there is an error upon importing.

    for( int i=0; i < number_of_data_entries ; i++ )

    {
		density = microenvironment(i)[nECM];

	    fwrite( (char*) &( microenvironment.mesh.voxels[i].center[0] ) , sizeof(double) , 1 , fp ); // 1

        fwrite( (char*) &( microenvironment.mesh.voxels[i].center[1] ) , sizeof(double) , 1 , fp ); // 2

        fwrite( (char*) &( microenvironment.mesh.voxels[i].center[2] ) , sizeof(double) , 1 , fp ); //3
		
		fwrite( (char*) &( density ), sizeof(double) , 1 , fp ); // 4

        // current voxel index of cell

    }



    fclose( fp );



    return;

}

void run_biotransport( double t_max )
{
	std::cout << "working on initial conditions .. " << std::endl; 
	double t = 0.0;
	
	// make sure the associated cell has the correct rate vectors 
	
	for( int i=0 ; i < (*all_cells).size() ; i++ )
	{
		Cell* pCell = (*all_cells)[i];
		
//			pCell->secretion_rates = &secretion_rates; 
//			pCell->uptake_rates = &uptake_rates; 
//			pCell->saturation_densities = &saturation_densities; 
			
			pCell->set_total_volume( pCell->phenotype.volume.total ); 
			pCell->set_internal_uptake_constants( diffusion_dt );
	}
	
	while( t < t_max )
	{
		microenvironment.simulate_diffusion_decay( diffusion_dt );
		#pragma omp parallel for 
		for( int i=0 ; i < (*all_cells).size() ; i++ )
		{
			(*all_cells)[i]->phenotype.secretion.advance( (*all_cells)[i] , (*all_cells)[i]->phenotype , diffusion_dt ) ;
		}
		t += diffusion_dt; 
	}
	std::cout << "done!" << std::endl; 
	return; 
}