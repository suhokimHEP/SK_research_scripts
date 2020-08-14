#include <math.h>
#include <string>
#include <iostream>
#include <dirent.h>

using namespace std;

float deltaR (Float_t eta1, Float_t phi1, Float_t eta2, Float_t phi2){
float deta = eta1-eta2;
float dphi = phi1-phi2;
if (abs(dphi)>3.14){dphi = 6.28-abs(dphi);}
float rad = std::sqrt(deta*deta+dphi*dphi);
return rad;
}

void SigGenMatch(){


gErrorIgnoreLevel = kBreak;
float cutdelta = 0.4;
vector<string> filelist;
//const char *path = "/eos/uscms/store/group/lpchbb/LLDJntuples/topRWT/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/crab_ZH_HToSSTobbbb_MS-55_ctauS-100/181004_091330/0000/";
const char *path = "/eos/uscms/store/group/lpchbb/LLDJntuples/2016_ctauReweightTest_2/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCUETP8M1_13TeV-powheg-pythia8/crab_ZH_HToSSTobbbb_MS-55_ctauS-100/200416_174554/0000/";
//const char *path = "/eos/uscms/store/group/lpchbb/LLDJntuples/2017_ctauReweightTest/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCP5_13TeV-powheg-pythia8/dir1/dir2/dir3/";
//const char *path = "/eos/uscms/store/group/lpchbb/LLDJntuples/2018_ctauReweightTest/ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100_TuneCP5_13TeV-powheg-pythia8/dir1/dir2/dir3/";
string sample ="ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100";
DIR *dir;
struct dirent *ent;
if ((dir = opendir (path)) != NULL) {
  /* print all the files and directories within directory */
  while ((ent = readdir (dir)) != NULL) {
    printf ("%s%s\n",path,ent->d_name);
    string subname = ent->d_name;
    string filename = path + subname;
    //std::cout<<filename<<std::endl;
	if(filename.find("root")!= std::string::npos){
    filelist.push_back(filename);}
  }
  closedir (dir);
}

TH1I* hgoodEvent = new TH1I("hgoodEvent","hgoodEvent",2, 0, 2);
TH1I* hGenMatched = new TH1I("hGenMatched","hGenMatched",2, 0, 2);
TH1F* hdeltaR = new TH1F("hdeltaR","hdeltaR",200, 0, 4);
TH1F* hAODCaloJetPt = new TH1F("hAODCaloJetPt","hAODCaloJetPt",250, 0, 500);
TH1F* hAODCaloJetEta = new TH1F("hAODCaloJetEta","hAODCaloJetEta",100, -5, 5);
TH1F* hAODCaloJetPhi = new TH1F("hAODCaloJetPhi","hAODCaloJetPhi",314, -3.14, 3.14);
TH1F* hAODCaloJetAlphaMax = new TH1F("hAODCaloJetAlphaMax","hAODCaloJetAlphaMax",120, 0, 1.2);
TH1F* hAODCaloJetMedianLog10IPSig = new TH1F("hAODCaloJetMedianLog10IPSig","hAODCaloJetMedianLog10IPSig",70, -3, 4);
TH1F* hAODCaloJetMedianLog10TrackAngle = new TH1F("hAODCaloJetMedianLog10TrackAngle","hAODCaloJetMedianLog10TrackAngle",70, -5, 2);
TH1F* h_GenMatched_AODCaloJetPt = new TH1F("h_GenMatched_AODCaloJetPt","h_GenMatched_AODCaloJetPt",250, 0, 500);
TH1F* h_GenMatched_AODCaloJetEta = new TH1F("h_GenMatched_AODCaloJetEta","h_GenMatched_AODCaloJetEta",100, -5, 5);
TH1F* h_GenMatched_AODCaloJetPhi = new TH1F("h_GenMatched_AODCaloJetPhi","h_GenMatched_AODCaloJetPhi",314, -3.14, 3.14);
TH1F* h_GenMatched_AODCaloJetAlphaMax = new TH1F("h_GenMatched_AODCaloJetAlphaMax","h_GenMatched_AODCaloJetAlphaMax",120, 0, 1.2);
TH1F* h_GenMatched_AODCaloJetMedianLog10IPSig = new TH1F("h_GenMatched_AODCaloJetMedianLog10IPSig","h_GenMatched_AODCaloJetMedianLog10IPSig",70, -3, 4);
TH1F* h_GenMatched_AODCaloJetMedianLog10TrackAngle = new TH1F("h_GenMatched_AODCaloJetMedianLog10TrackAngle","h_GenMatched_AODCaloJetMedianLog10TrackAngle",70, -5, 2);




for (int j=0; j<(int)filelist.size(); ++j)
{cout<<filelist[j]<<endl;
TFile* _file0; 
TTree* mytree ;
string conname = filelist[j];
conname = conname.substr(conname.find("/store")); 
conname = "root://cmsxrootd.fnal.gov/"+conname;
TString realname = conname;
_file0 = TFile::Open(realname,"read");
mytree = (TTree*)_file0->Get("lldjNtuple/EventTree");
//mytree->Print();
std::vector<float> *llpDaughtervX=0;
std::vector<float> *llpDaughtervY=0;
std::vector<float> *llpDaughterPt=0;
std::vector<float> *llpDaughterEta=0;
std::vector<float> *llpDaughterPhi=0;
std::vector<float> *llpDaughterMass=0;
std::vector<float> *llpDaughterStatus=0;
std::vector<float> *AODCaloJetPt=0;
std::vector<float> *AODCaloJetEta=0;
std::vector<float> *AODCaloJetPhi=0;
std::vector<float> *AODCaloJetAlphaMax=0;
std::vector<float> *AODCaloJetMedianLog10IPSig=0;
std::vector<float> *AODCaloJetMedianLog10TrackAngle=0;
mytree->SetBranchAddress("llpDaughtervX", &llpDaughtervX);
mytree->SetBranchAddress("llpDaughtervY", &llpDaughtervY);
mytree->SetBranchAddress("llpDaughterPt", &llpDaughterPt);
mytree->SetBranchAddress("llpDaughterEta", &llpDaughterEta);
mytree->SetBranchAddress("llpDaughterPhi", &llpDaughterPhi);
mytree->SetBranchAddress("llpDaughterMass", &llpDaughterMass);
mytree->SetBranchAddress("llpDaughterStatus", &llpDaughterStatus);
mytree->SetBranchAddress("AODCaloJetPt", &AODCaloJetPt);
mytree->SetBranchAddress("AODCaloJetEta", &AODCaloJetEta);
mytree->SetBranchAddress("AODCaloJetPhi", &AODCaloJetPhi);
mytree->SetBranchAddress("AODCaloJetAlphaMax", &AODCaloJetAlphaMax);
mytree->SetBranchAddress("AODCaloJetMedianLog10IPSig", &AODCaloJetMedianLog10IPSig);
mytree->SetBranchAddress("AODCaloJetMedianLog10TrackAngle", &AODCaloJetMedianLog10TrackAngle);
for (Int_t i=0;i<mytree->GetEntries(); i++) {
mytree->GetEntry(i);
Int_t llpDsize = llpDaughterStatus->size();


bool tracktrue = true;
for (Int_t ii=1;ii<5; ii++) {
float vX = llpDaughtervX->at(4-ii);
float vY = llpDaughtervY->at(4-ii);
float trackR = std::sqrt(vX*vX+vY*vY);
//cout<<trackR<<endl;
if (trackR<2.5||trackR>100.) {tracktrue = false;}
}
//cout<<tracktrue<<endl;

if (llpDaughterStatus->at(llpDsize-1)!=71||llpDaughterStatus->at(llpDsize-2)!=71||llpDaughterStatus->at(llpDsize-3)!=71||llpDaughterStatus->at(llpDsize-4)!=71)
	{
hgoodEvent->Fill(0);
continue;
	}

else if (tracktrue ==false)
	{
hgoodEvent->Fill(0);
continue;
	}

else {
	//std::cout<<"new good event"<<std::endl;
	hgoodEvent->Fill(1);
	for (Int_t j=0;j<AODCaloJetPt->size(); j++) {
	//std::cout<<"new jet"<<std::endl;
	std::vector<float> listR; 
	listR.clear();
	hAODCaloJetPt->Fill(AODCaloJetPt->at(j),1);
	hAODCaloJetEta->Fill(AODCaloJetEta->at(j),1);
	hAODCaloJetPhi->Fill(AODCaloJetPhi->at(j),1);
	hAODCaloJetAlphaMax->Fill(AODCaloJetAlphaMax->at(j),1);
	hAODCaloJetMedianLog10IPSig->Fill(AODCaloJetMedianLog10IPSig->at(j),1);
	hAODCaloJetMedianLog10TrackAngle->Fill(AODCaloJetMedianLog10TrackAngle->at(j),1);	
	for(Int_t k=1;k<5; k++){
	float delta = deltaR(AODCaloJetEta->at(j),AODCaloJetPhi->at(j),llpDaughterEta->at(llpDsize-k),llpDaughterPhi->at(llpDsize-k));
	listR.push_back(delta);
	}	
	//std::cout<<"new jet's smallest R"<<std::endl;
	float realR = *min_element(listR.begin(), listR.end());
	hdeltaR->Fill(realR,1);
	//std::cout<<realR<<std::endl;	
	if (realR < cutdelta)
	{
	hGenMatched->Fill(1);
	h_GenMatched_AODCaloJetPt->Fill(AODCaloJetPt->at(j),1);
	h_GenMatched_AODCaloJetEta->Fill(AODCaloJetEta->at(j),1);
	h_GenMatched_AODCaloJetPhi->Fill(AODCaloJetPhi->at(j),1);
	h_GenMatched_AODCaloJetAlphaMax->Fill(AODCaloJetAlphaMax->at(j),1);
	h_GenMatched_AODCaloJetMedianLog10IPSig->Fill(AODCaloJetMedianLog10IPSig->at(j),1);
	h_GenMatched_AODCaloJetMedianLog10TrackAngle->Fill(AODCaloJetMedianLog10TrackAngle->at(j),1);	
	} 	
	else{
	hGenMatched->Fill(0);
		}
	}
}
llpDaughterPt->clear();
llpDaughterEta->clear();
llpDaughterPhi->clear();
llpDaughterMass->clear();
llpDaughterStatus->clear();
AODCaloJetPt->clear();
AODCaloJetEta->clear();
AODCaloJetPhi->clear();
AODCaloJetAlphaMax->clear();
AODCaloJetMedianLog10IPSig->clear();
AODCaloJetMedianLog10TrackAngle->clear();
}
} 
TFile *newfile = new TFile("16GenMatch.root","recreate");
hgoodEvent->Write();
hGenMatched->Write();
hdeltaR->Write();
hAODCaloJetPt->Write();
hAODCaloJetEta->Write();
hAODCaloJetPhi->Write();
hAODCaloJetAlphaMax->Write();
hAODCaloJetMedianLog10IPSig->Write();
hAODCaloJetMedianLog10TrackAngle->Write();
h_GenMatched_AODCaloJetPt->Write();
h_GenMatched_AODCaloJetEta->Write();
h_GenMatched_AODCaloJetPhi->Write();
h_GenMatched_AODCaloJetAlphaMax->Write();
h_GenMatched_AODCaloJetMedianLog10IPSig->Write();
h_GenMatched_AODCaloJetMedianLog10TrackAngle->Write();
}


