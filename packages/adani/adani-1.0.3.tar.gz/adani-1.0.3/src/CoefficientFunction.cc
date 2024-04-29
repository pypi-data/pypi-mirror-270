#include "adani/CoefficientFunction.h"

using std::cout;
using std::endl;

//==========================================================================================//
//  CoefficientFunction: constructor
//------------------------------------------------------------------------------------------//

CoefficientFunction::CoefficientFunction(
    const int &order, const char &kind, const char &channel
)
    : order_(order), kind_(kind), channel_(channel) {

    // check order
    if (order < 1 || order > 3) {
        cout << "Error: order must be 1, 2 or 3. Got: " << order << endl;
        exit(-1);
    }

    // check kind
    if (kind != '2' && kind != 'L') {
        cout << "Error: kind must be 2 or L. Got: " << kind << endl;
        exit(-1);
    }

    // check channel
    if (channel != 'g' && channel != 'q') {
        cout << "Error: channel must be g or q. Got: " << channel << endl;
        exit(-1);
    }
    if (channel_ == 'q' && order_ == 1) {
        cout << "Error: quark coefficient function at O(as) doesn't exist!"
             << endl;
        exit(-1);
    }
}

//==========================================================================================//
//  CoefficientFunction: destructor
//------------------------------------------------------------------------------------------//

CoefficientFunction::~CoefficientFunction(){};

//==========================================================================================//
//  CoefficientFunction: central value of fx
//------------------------------------------------------------------------------------------//

double
    CoefficientFunction::fx(double x, double m2Q2, double m2mu2, int nf) const {
    return fxBand(x, m2Q2, m2mu2, nf).GetCentral();
}

//==========================================================================================//
//  CoefficientFunction: central value of mu independent terms
//------------------------------------------------------------------------------------------//

double CoefficientFunction::MuIndependentTerms(
    double x, double m2Q2, int nf
) const {
    return fx(x, m2Q2, 1., nf);
}

//==========================================================================================//
//  CoefficientFunction: central value mu dependent terms
//------------------------------------------------------------------------------------------//

double CoefficientFunction::MuDependentTerms(
    double x, double m2Q2, double m2mu2, int nf
) const {
    return fx(x, m2Q2, m2mu2, nf) - MuIndependentTerms(x, m2Q2, nf);
}

//==========================================================================================//
//  CoefficientFunction: band for mu independent terms
//------------------------------------------------------------------------------------------//

Value CoefficientFunction::MuIndependentTermsBand(
    double x, double m2Q2, int nf
) const {
    return fxBand(x, m2Q2, 1., nf);
    ;
}

//==========================================================================================//
//  CoefficientFunction: band for mu dependent terms
//------------------------------------------------------------------------------------------//

Value CoefficientFunction::MuDependentTermsBand(
    double x, double m2Q2, double m2mu2, int nf
) const {

    double central = fxBand(x, m2Q2, m2mu2, nf).GetCentral()
                     - MuIndependentTermsBand(x, m2Q2, nf).GetCentral();
    double higher = fxBand(x, m2Q2, m2mu2, nf).GetHigher()
                    - MuIndependentTermsBand(x, m2Q2, nf).GetHigher();
    double lower = fxBand(x, m2Q2, m2mu2, nf).GetLower()
                   - MuIndependentTermsBand(x, m2Q2, nf).GetLower();

    return Value(central, higher, lower);
}
