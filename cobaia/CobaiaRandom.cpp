#include "CobaiaRandom.h"

bool CobaiaRandom::run(const Rsyn::Json &params) {
	this->session = session; // highly necessary (do not forget)
	// this->design = session.getDesign(); // not necessary (so far)
	this->module = session.getTopModule(); // get instances
	this->phDesign = session.getPhysicalDesign(); // get and set cells position
	
	expecto_patronum(); // or "run forrest!" or "fire in the hole" or "engage"

	return true;
}

void CobaiaRandom::random_initial_placement() {
	
	Rsyn::PhysicalModule phModule = phDesign.getPhysicalModule(module);
	
	// Core spatial coordinates x1,y1,x2,y2 (@see Bounds)
	const Bounds &coreBounds = phModule.getBounds();
	const int64_t height = coreBounds.getHeight();
	cout << "Core Bounds: " << coreBounds << endl;
	cout << "Row Height: " << phDesign.getRowHeight() << endl;

	const int64_t rowHeight = phDesign.getRowHeight();

	module.data;

	for (Rsyn::Instance instance : module.allInstances()) { // other possibilities: allNets?

		if (instance.getType() != Rsyn::CELL) continue;

		Rsyn::Cell aCell = instance.asCell(); // CAST?!
		Rsyn::PhysicalCell cell = phDesign.getPhysicalCell(aCell);		
		
		if ( ! (instance.isFixed() || instance.isMacroBlock()) ) {

			const Bounds cellBounds = cell.getBounds();
			DBU rand_x = 0; //coreBounds.getX() + rand() % coreBounds.getWidth();
			DBU rand_y = 0; // coreBounds.getY() + rand() % coreBounds.getHeight();
			
			do { // ensure rand within core bounds
				rand_x = coreBounds.getX() + rand() % coreBounds.getWidth();
			} while (rand_x + cellBounds.getUpper().x > coreBounds.getWidth());
			
			do { // ensure rand within core bounds
				// randomizing the row
				rand_y = coreBounds.getY() + rand() % phDesign.getNumRows() * phDesign.getRowHeight();
				//rand_y = coreBounds.getY() + rand() % coreBounds.getHeight();
			} while (rand_y + cellBounds.getUpper().y > coreBounds.getHeight());

			// cout << "rand_x " << rand_x << ", rand_y " << rand_y << endl;
			phDesign.placeCell(cell, rand_x, rand_y);

		}
	}
	cout << "Wirelength before random placement: " << phDesign.getHPWL() << endl;
	phDesign.updateAllNetBounds(1);
	cout << "Wirelength after random placement: " << phDesign.getHPWL() << endl;

	

	// for (Rsyn::Net n : module.allNets()) phDesign.updateNetBound(n);
	// cout << "Wirelength: " << phDesign.getHPWL() << endl;
	// phDesign.updateAllNetBounds(1);
	// cout << "Wirelength: " << phDesign.getHPWL() << endl;
}

void CobaiaRandom::expecto_patronum() {
	
	random_initial_placement();

}

