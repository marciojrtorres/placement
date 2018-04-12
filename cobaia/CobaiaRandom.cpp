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
	for (Rsyn::Instance instance : module.allInstances()) { // other possibilities: allNets?
		if (instance.getType() != Rsyn::CELL) continue;
		Rsyn::Cell aCell = instance.asCell(); // CAST?!
		Rsyn::PhysicalCell cell = phDesign.getPhysicalCell(aCell);		
		if ( ! (instance.isFixed() || instance.isMacroBlock()) ) {
			// typedef std::int64_t DBU;
			DBU rand_x = coreBounds.getX() + rand() % coreBounds.getWidth();
			DBU rand_y = coreBounds.getY() + rand() % coreBounds.getHeight();
			cout << "rand_x " << rand_x << ", rand_y " << rand_y << endl;
			phDesign.placeCell(cell, rand_x, rand_y);
			// phDesign.placeCell(cell, 90000, 80000);
		}
	}
	// how to traverse the netlist?
	for (Rsyn::Instance instance : module.allInstances()) {
		for (Rsyn::Pin pin : instance.allPins()) {
			Rsyn::Cell cell = pin.getInstance().asCell();
			cout << "CELL " << cell.getName() << endl;
			// how to compute the wirelength?
		}
	}
}

void CobaiaRandom::expecto_patronum() {
	
	random_initial_placement();

}

