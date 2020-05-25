#include "LLDJstandalones/ntuples/interface/lldjNtuple.h"
#include "LLDJstandalones/ntuples/interface/GenParticleParentage.h"
#include <TMath.h>
#include <TLorentzVector.h>

using namespace std;
bool ctauWeight = false; //Determine whether to weight or not weight the SigMC
float targetdist = 300; //To weight it, determine the target distance
//Recommended targetdist range : 10mm sample->1mm<ct<10mm
			//	 100mm sample->10mm<ct<100mm
			//	 1000mm	samplet->100mm<ct<1000mm


//Variables for branches
vector<int>   llpId;
vector<int>   llpStatus;
vector<float> llpPt;
vector<float> llpEta;
vector<float> llpPhi;
vector<float> llpMass;
vector<int>   eleId;
vector<int>   eleStatus;
vector<float> elePt;
vector<float> eleEta;
vector<float> elePhi;
vector<float> eleMass;
vector<int>   muId;
vector<int>   muStatus;
vector<float> muPt;
vector<float> muEta;
vector<float> muPhi;
vector<float> muMass;
vector<float> DiElePass;
vector<float> DiMuPass;
vector<int>   llpDaughterId;
vector<int>   llpDaughterStatus;
vector<float> llpDaughterPt;
vector<float> llpDaughterEta;
vector<float> llpDaughterPhi;
vector<float> llpDaughterMass;
vector<float> toppts;
vector<float> Decaydist;
vector<float> Simweight;
float ctauEventWeight;
int eventnumber;
void lldjNtuple::branchesGenPart(TTree* tree) {

  tree->Branch("llpId",             &llpId);
  tree->Branch("llpStatus",         &llpStatus);
  tree->Branch("llpPt",             &llpPt);
  tree->Branch("llpEta",            &llpEta);
  tree->Branch("llpPhi",            &llpPhi);
  tree->Branch("llpMass",           &llpMass);
  tree->Branch("eleId",             &eleId);
  tree->Branch("eleStatus",         &eleStatus);
  tree->Branch("elePt",             &elePt);
  tree->Branch("eleEta",            &eleEta);
  tree->Branch("elePhi",            &elePhi);
  tree->Branch("eleMass",           &eleMass);
  tree->Branch("muId",             &muId);
  tree->Branch("muStatus",         &muStatus);
  tree->Branch("muPt",             &muPt);
  tree->Branch("muEta",            &muEta);
  tree->Branch("muPhi",            &muPhi);
  tree->Branch("muMass",           &muMass);
  tree->Branch("DiElePass",           &DiElePass);
  tree->Branch("DiMuPass",           &DiMuPass);
  tree->Branch("llpDaughterPt",     &llpDaughterPt);
  tree->Branch("llpDaughterEta",    &llpDaughterEta);
  tree->Branch("llpDaughterPhi",    &llpDaughterPhi);
  tree->Branch("llpDaughterMass",   &llpDaughterMass);
  tree->Branch("toppts",            &toppts);
  if (ctauWeight) {tree->Branch("Decaydist",         &Decaydist);
  tree->Branch("Simweight",         &Simweight);
  tree->Branch("ctauEventWeight",   &ctauEventWeight);
}
}

void lldjNtuple::fillGenPart(const edm::Event& e) {
  eventnumber +=1;
  //Initialize -- set numbers to e.g. 0 and clear vectors 
  llpId.clear();
  llpStatus.clear();
  llpPt.clear();
  llpEta.clear();
  llpPhi.clear();
  llpMass.clear();
  eleId.clear();
  eleStatus.clear();
  elePt.clear();
  eleEta.clear();
  elePhi.clear();
  eleMass.clear();
  muId.clear();
  muStatus.clear();
  muPt.clear();
  muEta.clear();
  muPhi.clear();
  muMass.clear();
  DiElePass.clear();
  DiMuPass.clear();
  llpDaughterId.clear();
  llpDaughterStatus.clear();
  llpDaughterPt.clear();
  llpDaughterEta.clear();
  llpDaughterPhi.clear();
  llpDaughterMass.clear();
  toppts.clear();
  if (ctauWeight){Decaydist.clear();
  Simweight.clear();
  ctauEventWeight=1.0;
}
  //Gen particles handle
  edm::Handle<vector<reco::GenParticle> > genParticlesHandle;
  e.getByToken(genParticlesCollection_, genParticlesHandle);
  float totEventWeight =1.0;
  int Znumber =0;
  //std::cout<<"new event"<<std::endl;
  //Loop over gen particles
  for (vector<reco::GenParticle>::const_iterator ip = genParticlesHandle->begin(); ip != genParticlesHandle->end(); ++ip) {
     //std::cout<<"new particle:"<<ip->pdgId()<<std::endl; 
    reco::GenParticleRef partRef = reco::GenParticleRef(genParticlesHandle,
							ip-genParticlesHandle->begin());
    genpartparentage::GenParticleParentage particleHistory(partRef);
     //std::cout<<"When new particle"<<std::endl; 
    if (ip->pdgId()==23) {}
    //Save top particles
    if( abs(ip->pdgId()) == 6 && ip->isLastCopy() ){
     toppts.push_back( ip->pt() );
    }
    //Save ele and mu kinematic variables for investigation of lepton efficiency	 
    if ( particleHistory.hasRealParent() ) {
      reco::GenParticleRef momRef = particleHistory.parent();
      if ( momRef.isNonnull() && momRef.isAvailable() ) {
	if( abs(momRef->pdgId()) == 23 && abs(ip->pdgId()) == 11 ){
	  eleId.push_back(     ip->pdgId() );
	  eleStatus.push_back( ip->status() );
	  elePt.push_back(     ip->pt()    );
	  eleEta.push_back(    ip->eta()   );
	  elePhi.push_back(    ip->phi()   );
	  eleMass.push_back(   ip->mass()  );
	}
	if( abs(momRef->pdgId()) == 23 && abs(ip->pdgId()) == 13 ){
	  muId.push_back(     ip->pdgId() );
	  muStatus.push_back( ip->status() );
	  muPt.push_back(     ip->pt()    );
	  muEta.push_back(    ip->eta()   );
	  muPhi.push_back(    ip->phi()   );
	  muMass.push_back(   ip->mass()  );

	}
	}	
	}
    
    //Save long lived BSM particles
    if( abs(ip->pdgId()) == 9000006 ){
      llpId.push_back(      ip->pdgId() );
      llpStatus.push_back(  ip->status() );
      llpPt.push_back(      ip->pt()    );
      llpEta.push_back(     ip->eta()   );
      llpPhi.push_back(     ip->phi()   );
      llpMass.push_back(    ip->mass()  );
      TVector3 mother,daughter,diff;	
      for(size_t j=0; j<ip->numberOfDaughters(); ++j){
	const reco::Candidate* d = ip->daughter(j);
	  mother.SetXYZ(ip->vx(),ip->vy(),ip->vz());
	  daughter.SetXYZ(d->vx(),d->vy(),d->vz());
   	  diff.SetXYZ(mother.X()-daughter.X(),mother.Y()-daughter.Y(),mother.Z()-daughter.Z());	
	} 

	TLorentzVector scalar;
	scalar.SetPtEtaPhiM(ip->pt(),ip->eta(),ip->phi(),ip->mass());
	float dist = diff.Mag()/(scalar.Gamma()*abs(scalar.Beta()));
        if(ctauWeight){Decaydist.push_back(dist);
	float weight = calculatectauEventWeight(dist);
	Simweight.push_back(weight); 
        totEventWeight *= weight;}
    }
    else if ( particleHistory.hasRealParent() ) {
      reco::GenParticleRef momRef = particleHistory.parent();
      if ( momRef.isNonnull() && momRef.isAvailable() ) {
	if( abs(momRef->pdgId()) == 9000006 ){
	  llpDaughterId.push_back(     ip->pdgId() );
	  llpDaughterStatus.push_back( ip->status() );
	  llpDaughterPt.push_back(     ip->pt()    );
	  llpDaughterEta.push_back(    ip->eta()   );
	  llpDaughterPhi.push_back(    ip->phi()   );
	  llpDaughterMass.push_back(   ip->mass()  );
	}
      }
    }

  }//end gen loop
//if (elePt.size()<2 && muPt.size()<2) {std::cout<<"This event has only_"<<elePt.size()<<"electrons and"<<muPt.size()<<"from Z boson with event number"<<eventnumber<<std::endl;} 
//if (elePt.size()<2 && muPt.size()<2) {std::cout<<"This event has only_"<<Znumber<<"Z boson with event number"<<eventnumber<<std::endl;} 
  //Checking Gen-level lepton Pt,Eta Efficiency
    GenLeptEffi( elePt, eleEta, muPt, muEta);
 
  //TT Scale Factor
  float TTSF = 1.;
  if(toppts.size() == 2){
   TTSF = TTSF * exp( 0.0615 - 0.0005*toppts.at(0)) * exp( 0.0615 - 0.0005*toppts.at(1));
  }
  hTTSF_->Fill( TTSF );
  //std::cout<<"TTSF   "<<TTSF<<std::endl;

  //ctauEventWeight
  if(ctauWeight) ctauEventWeight = totEventWeight;

}

Float_t lldjNtuple::calculatectauEventWeight( float dist )
{
 float weight, factor;
if (targetdist<10 && 1 < targetdist) {
	factor = 10./targetdist;
        weight = factor*exp(-1*(factor-1)*dist);
}
else if (targetdist<100 && 10 < targetdist) {
	factor = 100./targetdist;
        weight = factor*exp(-0.1*(factor-1)*dist);
}

else if (targetdist<1000 && 100< targetdist) {
	factor = 1000./targetdist;
        weight = factor*exp(-0.01*(factor-1)*dist);
}
else  {   
    std::cerr << "Targetdist out of range. Please read insturction for targetdist range for each SigMC sample." <<std::endl;
   abort(); 	
	}
 return weight;
 }

void lldjNtuple::GenLeptEffi( vector<float> elePt, vector<float> eleEta, vector<float> muPt,vector<float> muEta)
{
  //Checking Gen-level lepton Pt,Eta Efficiency
  std::vector<int> elelist, mulist;
  for(unsigned int i = 0; i < elePt.size(); i++){elelist.push_back(i);}
  for(unsigned int i = 0; i < muPt.size(); i++){mulist.push_back(i);}
  std::sort(elelist.begin(),elelist.end(), 
           [&]( int a, int b ) { return elePt.at(a) > elePt.at(b); });
  std::sort(mulist.begin(),mulist.end(), 
           [&]( int a, int b ) { return muPt.at(a) > muPt.at(b); });

  if(elelist.size()>1) {
   if(elePt.at(elelist[0])>25. && abs(eleEta.at(elelist[0]))<2.5 &&  !(abs(eleEta.at(elelist[0]))>1.442 && abs(eleEta.at(elelist[0]))<1.556)
       && elePt.at(elelist[1])>15. && abs(eleEta.at(elelist[1]))<2.5 &&  !(abs(eleEta.at(elelist[0]))>1.442 && abs(eleEta.at(elelist[0]))<1.556)) {DiElePass.push_back(1.);}
    else {DiElePass.push_back(0.);}}

  if(mulist.size()>1) {
   if(muPt.at(mulist[0])>25. && abs(muEta.at(mulist[0]))<2.5
       && muPt.at(mulist[1])>15. && abs(muEta.at(mulist[1]))<2.5) {DiMuPass.push_back(1.);}
    else {DiMuPass.push_back(0.);}}
 }

