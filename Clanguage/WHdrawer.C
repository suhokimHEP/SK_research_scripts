#include <iostream>
#include <fstream>
#include <unistd.h>

#include "TROOT.h"
#include <TChain.h>
#include <TString.h>
#include <TStopwatch.h>
 
#include <vector>
#include <map>

//int main(int argc, char **argv){
int drawer(TString sample, TString inpath, TString outpath, TString nfiles, TString atfile){
 std::cout << "Running sample: " << sample << std::endl;

 // easiest if we convert char to TString
 TString Tsample  = TString(sample);
 TString Tinpath  = TString(inpath);  
 TString Toutpath = TString(outpath); 
 TString TSnfiles = TString(nfiles);
 TString TSatfile = TString(atfile);  
 Int_t   TInfiles = TSnfiles.Atoi();
 Int_t   TIatfile = TSatfile.Atoi();

 std::cout << "Tsample: " << Tsample << std::endl;
 std::cout << "TInfiles: " << TInfiles << std::endl;

 Bool_t makelog=kFALSE;

 //TString outfilename=Toutpath +"/"+Tsample;
 TString outfilename=Tsample+"_"+Toutpath;
 TString inputListName=Tinpath+"/"+Tsample+".list";
 TString inputInfoName=Tinpath+"/"+Tsample+".info";

 TChain *theChain = new TChain("TreeMakerMINIAOD/HiggsLongLived");
 theChain->Reset();
 TChain *trigChain = new TChain("TreeMakerMINIAOD/TriggerInfo");
 trigChain->Reset();

 std::cout << "Input List Name: " << inputListName << std::endl;
 std::cout << "Output File Name: " << outfilename << std::endl;

 // lines read from file variables
 std::string inputline = "";
 TString Tinputline = "";
 std::vector<TString> inputline_dump;

 // ---- Get list of files to run over and put in TChain
 // open <samplename>.list
 std::ifstream inputfile;
 inputfile.open(inputListName);
 if( !inputfile.good() ) {
   std::cerr << "Cannot open the file: \"" << inputListName+"\""<<std::endl;
   abort();
 }
 
 // For dividing up input list
 Int_t nscanned = 0; // number of files scanned so far
 // we have the file open, start reading lines one by one
 while( std::getline(inputfile, inputline) ) {
  if( inputfile.fail() ) continue;

  // we have a flag to decide which file to start at
  nscanned++;
  if ( nscanned < TIatfile ) continue;
  if ( nscanned >= (TIatfile+TInfiles) ) continue;
  //if ( nscanned >= TInfiles ) continue;

  // TChain needs a TString..
  Tinputline = inputline;
  std::cout << "raw inputline: " << Tinputline << std::endl;

  // read input file names
  if( Tinputline.Contains("/uscms/home") ){
   theChain->Add( Tinputline );
   std::cout << " Inputfile: " << Tinputline << std::endl;
  }

  if( Tinputline.Contains("/store/group") ){
   theChain->Add( "root://cmsxrootd.fnal.gov/"+Tinputline );
   trigChain->Add( "root://cmsxrootd.fnal.gov/"+Tinputline );
   std::cout << " Inputfile: " << Tinputline << std::endl;
  }



  inputline_dump.push_back(inputline);
 } // while( std::getline(inputfile, inputline) )
 inputfile.close();

 //////////////////////////////////////////////////////////////////
  TTree *MS7ct1tree_ = new TTree("MS7ct1tree","MS7ct1tree");
  TTree *MS7ct10tree_ = new TTree("MS7ct10tree","MS7ct10tree");
  TTree *MS7ct100tree_ = new TTree("MS7ct100tree","MS7ct100tree");
  TTree *MS7ct1000tree_ = new TTree("MS7ct1000tree","MS7ct1000tree");
  TTree *MS15ct1tree_ = new TTree("MS15ct1tree","MS15ct1tree");
  TTree *MS15ct10tree_ = new TTree("MS15ct10tree","MS15ct10tree");
  TTree *MS15ct100tree_ = new TTree("MS15ct100tree","MS15ct100tree");
  TTree *MS15ct1000tree_ = new TTree("MS15ct1000tree","MS15ct1000tree");
  TTree *MS40ct1tree_ = new TTree("MS40ct1tree","MS40ct1tree");
  TTree *MS40ct10tree_ = new TTree("MS40ct10tree","MS40ct10tree");
  TTree *MS40ct100tree_ = new TTree("MS40ct100tree","MS40ct100tree");
  TTree *MS40ct1000tree_ = new TTree("MS40ct1000tree","MS40ct1000tree");

  ULong64_t   MS7ct1_HLT_Ele23Loose_;
  ULong64_t   MS7ct10_HLT_Ele23Loose_;
  ULong64_t   MS7ct100_HLT_Ele23Loose_;
  ULong64_t   MS7ct1000_HLT_Ele23Loose_;
  ULong64_t   MS15ct1_HLT_Ele23Loose_;
  ULong64_t   MS15ct10_HLT_Ele23Loose_;
  ULong64_t   MS15ct100_HLT_Ele23Loose_;
  ULong64_t   MS15ct1000_HLT_Ele23Loose_;
  ULong64_t   MS40ct1_HLT_Ele23Loose_;
  ULong64_t   MS40ct10_HLT_Ele23Loose_;
  ULong64_t   MS40ct100_HLT_Ele23Loose_;
  ULong64_t   MS40ct1000_HLT_Ele23Loose_;
  ULong64_t   MS7ct1_HLT_Ele23Ele12_;
  ULong64_t   MS7ct10_HLT_Ele23Ele12_;
  ULong64_t   MS7ct100_HLT_Ele23Ele12_;
  ULong64_t   MS7ct1000_HLT_Ele23Ele12_;
  ULong64_t   MS15ct1_HLT_Ele23Ele12_;
  ULong64_t   MS15ct10_HLT_Ele23Ele12_;
  ULong64_t   MS15ct100_HLT_Ele23Ele12_;
  ULong64_t   MS15ct1000_HLT_Ele23Ele12_;
  ULong64_t   MS40ct1_HLT_Ele23Ele12_;
  ULong64_t   MS40ct10_HLT_Ele23Ele12_;
  ULong64_t   MS40ct100_HLT_Ele23Ele12_;
  ULong64_t   MS40ct1000_HLT_Ele23Ele12_;
  ULong64_t   MS7ct1_HLT_IsoTkMu22_;
  ULong64_t   MS7ct10_HLT_IsoTkMu22_;
  ULong64_t   MS7ct100_HLT_IsoTkMu22_;
  ULong64_t   MS7ct1000_HLT_IsoTkMu22_;
  ULong64_t   MS15ct1_HLT_IsoTkMu22_;
  ULong64_t   MS15ct10_HLT_IsoTkMu22_;
  ULong64_t   MS15ct100_HLT_IsoTkMu22_;
  ULong64_t   MS15ct1000_HLT_IsoTkMu22_;
  ULong64_t   MS40ct1_HLT_IsoTkMu22_;
  ULong64_t   MS40ct10_HLT_IsoTkMu22_;
  ULong64_t   MS40ct100_HLT_IsoTkMu22_;
  ULong64_t   MS40ct1000_HLT_IsoTkMu22_;
  ULong64_t   MS7ct1_HLT_Mu17Mu8_;
  ULong64_t   MS7ct10_HLT_Mu17Mu8_;
  ULong64_t   MS7ct100_HLT_Mu17Mu8_;
  ULong64_t   MS7ct1000_HLT_Mu17Mu8_;
  ULong64_t   MS15ct1_HLT_Mu17Mu8_;
  ULong64_t   MS15ct10_HLT_Mu17Mu8_;
  ULong64_t   MS15ct100_HLT_Mu17Mu8_;
  ULong64_t   MS15ct1000_HLT_Mu17Mu8_;
  ULong64_t   MS40ct1_HLT_Mu17Mu8_;
  ULong64_t   MS40ct10_HLT_Mu17Mu8_;
  ULong64_t   MS40ct100_HLT_Mu17Mu8_;
  ULong64_t   MS40ct1000_HLT_Mu17Mu8_;
  ULong64_t   MS7ct1_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS7ct10_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS7ct100_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS7ct1000_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS15ct1_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS15ct10_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS15ct100_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS15ct1000_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS40ct1_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS40ct10_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS40ct100_HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   MS40ct1000_HLT_LooseTau50_Trk30_eta2p1_;

  ULong64_t   MS7ct1_HLT_Mu7IP4_;
  ULong64_t   MS7ct10_HLT_Mu7IP4_;
  ULong64_t   MS7ct100_HLT_Mu7IP4_;
  ULong64_t   MS7ct1000_HLT_Mu7IP4_;
  ULong64_t   MS15ct1_HLT_Mu7IP4_;
  ULong64_t   MS15ct10_HLT_Mu7IP4_;
  ULong64_t   MS15ct100_HLT_Mu7IP4_;
  ULong64_t   MS15ct1000_HLT_Mu7IP4_;
  ULong64_t   MS40ct1_HLT_Mu7IP4_;
  ULong64_t   MS40ct10_HLT_Mu7IP4_;
  ULong64_t   MS40ct100_HLT_Mu7IP4_;
  ULong64_t   MS40ct1000_HLT_Mu7IP4_;
  ULong64_t   MS7ct1_HLT_Mu8IP3_;
  ULong64_t   MS7ct10_HLT_Mu8IP3_;
  ULong64_t   MS7ct100_HLT_Mu8IP3_;
  ULong64_t   MS7ct1000_HLT_Mu8IP3_;
  ULong64_t   MS15ct1_HLT_Mu8IP3_;
  ULong64_t   MS15ct10_HLT_Mu8IP3_;
  ULong64_t   MS15ct100_HLT_Mu8IP3_;
  ULong64_t   MS15ct1000_HLT_Mu8IP3_;
  ULong64_t   MS40ct1_HLT_Mu8IP3_;
  ULong64_t   MS40ct10_HLT_Mu8IP3_;
  ULong64_t   MS40ct100_HLT_Mu8IP3_;
  ULong64_t   MS40ct1000_HLT_Mu8IP3_;
  ULong64_t   MS7ct1_HLT_Mu8IP6_;
  ULong64_t   MS7ct10_HLT_Mu8IP6_;
  ULong64_t   MS7ct100_HLT_Mu8IP6_;
  ULong64_t   MS7ct1000_HLT_Mu8IP6_;
  ULong64_t   MS15ct1_HLT_Mu8IP6_;
  ULong64_t   MS15ct10_HLT_Mu8IP6_;
  ULong64_t   MS15ct100_HLT_Mu8IP6_;
  ULong64_t   MS15ct1000_HLT_Mu8IP6_;
  ULong64_t   MS40ct1_HLT_Mu8IP6_;
  ULong64_t   MS40ct10_HLT_Mu8IP6_;
  ULong64_t   MS40ct100_HLT_Mu8IP6_;
  ULong64_t   MS40ct1000_HLT_Mu8IP6_;
  ULong64_t   MS7ct1_HLT_Mu9IP6_;
  ULong64_t   MS7ct10_HLT_Mu9IP6_;
  ULong64_t   MS7ct100_HLT_Mu9IP6_;
  ULong64_t   MS7ct1000_HLT_Mu9IP6_;
  ULong64_t   MS15ct1_HLT_Mu9IP6_;
  ULong64_t   MS15ct10_HLT_Mu9IP6_;
  ULong64_t   MS15ct100_HLT_Mu9IP6_;
  ULong64_t   MS15ct1000_HLT_Mu9IP6_;
  ULong64_t   MS40ct1_HLT_Mu9IP6_;
  ULong64_t   MS40ct10_HLT_Mu9IP6_;
  ULong64_t   MS40ct100_HLT_Mu9IP6_;
  ULong64_t   MS40ct1000_HLT_Mu9IP6_;
  ULong64_t   MS7ct1_HLT_Mu12IP6_;
  ULong64_t   MS7ct10_HLT_Mu12IP6_;
  ULong64_t   MS7ct100_HLT_Mu12IP6_;
  ULong64_t   MS7ct1000_HLT_Mu12IP6_;
  ULong64_t   MS15ct1_HLT_Mu12IP6_;
  ULong64_t   MS15ct10_HLT_Mu12IP6_;
  ULong64_t   MS15ct100_HLT_Mu12IP6_;
  ULong64_t   MS15ct1000_HLT_Mu12IP6_;
  ULong64_t   MS40ct1_HLT_Mu12IP6_;
  ULong64_t   MS40ct10_HLT_Mu12IP6_;
  ULong64_t   MS40ct100_HLT_Mu12IP6_;
  ULong64_t   MS40ct1000_HLT_Mu12IP6_;









MS7ct1tree_->Branch("MS7ct1_HLT_Ele23Loose",&MS7ct1_HLT_Ele23Loose_);
MS7ct10tree_->Branch("MS7ct10_HLT_Ele23Loose",&MS7ct10_HLT_Ele23Loose_);
MS7ct100tree_->Branch("MS7ct100_HLT_Ele23Loose",&MS7ct100_HLT_Ele23Loose_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_Ele23Loose",&MS7ct1000_HLT_Ele23Loose_);
MS15ct1tree_->Branch("MS15ct1_HLT_Ele23Loose",&MS15ct1_HLT_Ele23Loose_);
MS15ct10tree_->Branch("MS15ct10_HLT_Ele23Loose",&MS15ct10_HLT_Ele23Loose_);
MS15ct100tree_->Branch("MS15ct100_HLT_Ele23Loose",&MS15ct100_HLT_Ele23Loose_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_Ele23Loose",&MS15ct1000_HLT_Ele23Loose_);
MS40ct1tree_->Branch("MS40ct1_HLT_Ele23Loose",&MS40ct1_HLT_Ele23Loose_);
MS40ct10tree_->Branch("MS40ct10_HLT_Ele23Loose",&MS40ct10_HLT_Ele23Loose_);
MS40ct100tree_->Branch("MS40ct100_HLT_Ele23Loose",&MS40ct100_HLT_Ele23Loose_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_Ele23Loose",&MS40ct1000_HLT_Ele23Loose_);

MS7ct1tree_->Branch("MS7ct1_HLT_Ele23Ele12",&MS7ct1_HLT_Ele23Ele12_);
MS7ct10tree_->Branch("MS7ct10_HLT_Ele23Ele12",&MS7ct10_HLT_Ele23Ele12_);
MS7ct100tree_->Branch("MS7ct100_HLT_Ele23Ele12",&MS7ct100_HLT_Ele23Ele12_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_Ele23Ele12",&MS7ct1000_HLT_Ele23Ele12_);
MS15ct1tree_->Branch("MS15ct1_HLT_Ele23Ele12",&MS15ct1_HLT_Ele23Ele12_);
MS15ct10tree_->Branch("MS15ct10_HLT_Ele23Ele12",&MS15ct10_HLT_Ele23Ele12_);
MS15ct100tree_->Branch("MS15ct100_HLT_Ele23Ele12",&MS15ct100_HLT_Ele23Ele12_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_Ele23Ele12",&MS15ct1000_HLT_Ele23Ele12_);
MS40ct1tree_->Branch("MS40ct1_HLT_Ele23Ele12",&MS40ct1_HLT_Ele23Ele12_);
MS40ct10tree_->Branch("MS40ct10_HLT_Ele23Ele12",&MS40ct10_HLT_Ele23Ele12_);
MS40ct100tree_->Branch("MS40ct100_HLT_Ele23Ele12",&MS40ct100_HLT_Ele23Ele12_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_Ele23Ele12",&MS40ct1000_HLT_Ele23Ele12_);

MS7ct1tree_->Branch("MS7ct1_HLT_IsoTkMu22",&MS7ct1_HLT_IsoTkMu22_);
MS7ct10tree_->Branch("MS7ct10_HLT_IsoTkMu22",&MS7ct10_HLT_IsoTkMu22_);
MS7ct100tree_->Branch("MS7ct100_HLT_IsoTkMu22",&MS7ct100_HLT_IsoTkMu22_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_IsoTkMu22",&MS7ct1000_HLT_IsoTkMu22_);
MS15ct1tree_->Branch("MS15ct1_HLT_IsoTkMu22",&MS15ct1_HLT_IsoTkMu22_);
MS15ct10tree_->Branch("MS15ct10_HLT_IsoTkMu22",&MS15ct10_HLT_IsoTkMu22_);
MS15ct100tree_->Branch("MS15ct100_HLT_IsoTkMu22",&MS15ct100_HLT_IsoTkMu22_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_IsoTkMu22",&MS15ct1000_HLT_IsoTkMu22_);
MS40ct1tree_->Branch("MS40ct1_HLT_IsoTkMu22",&MS40ct1_HLT_IsoTkMu22_);
MS40ct10tree_->Branch("MS40ct10_HLT_IsoTkMu22",&MS40ct10_HLT_IsoTkMu22_);
MS40ct100tree_->Branch("MS40ct100_HLT_IsoTkMu22",&MS40ct100_HLT_IsoTkMu22_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_IsoTkMu22",&MS40ct1000_HLT_IsoTkMu22_);



MS7ct1tree_->Branch("MS7ct1_HLT_Mu17Mu8",&MS7ct1_HLT_Mu17Mu8_);
MS7ct10tree_->Branch("MS7ct10_HLT_Mu17Mu8",&MS7ct10_HLT_Mu17Mu8_);
MS7ct100tree_->Branch("MS7ct100_HLT_Mu17Mu8",&MS7ct100_HLT_Mu17Mu8_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_Mu17Mu8",&MS7ct1000_HLT_Mu17Mu8_);
MS15ct1tree_->Branch("MS15ct1_HLT_Mu17Mu8",&MS15ct1_HLT_Mu17Mu8_);
MS15ct10tree_->Branch("MS15ct10_HLT_Mu17Mu8",&MS15ct10_HLT_Mu17Mu8_);
MS15ct100tree_->Branch("MS15ct100_HLT_Mu17Mu8",&MS15ct100_HLT_Mu17Mu8_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_Mu17Mu8",&MS15ct1000_HLT_Mu17Mu8_);
MS40ct1tree_->Branch("MS40ct1_HLT_Mu17Mu8",&MS40ct1_HLT_Mu17Mu8_);
MS40ct10tree_->Branch("MS40ct10_HLT_Mu17Mu8",&MS40ct10_HLT_Mu17Mu8_);
MS40ct100tree_->Branch("MS40ct100_HLT_Mu17Mu8",&MS40ct100_HLT_Mu17Mu8_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_Mu17Mu8",&MS40ct1000_HLT_Mu17Mu8_);

MS7ct1tree_->Branch("MS7ct1_HLT_LooseTau50_Trk30_eta2p1",&MS7ct1_HLT_LooseTau50_Trk30_eta2p1_);
MS7ct10tree_->Branch("MS7ct10_HLT_LooseTau50_Trk30_eta2p1",&MS7ct10_HLT_LooseTau50_Trk30_eta2p1_);
MS7ct100tree_->Branch("MS7ct100_HLT_LooseTau50_Trk30_eta2p1",&MS7ct100_HLT_LooseTau50_Trk30_eta2p1_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_LooseTau50_Trk30_eta2p1",&MS7ct1000_HLT_LooseTau50_Trk30_eta2p1_);
MS15ct1tree_->Branch("MS15ct1_HLT_LooseTau50_Trk30_eta2p1",&MS15ct1_HLT_LooseTau50_Trk30_eta2p1_);
MS15ct10tree_->Branch("MS15ct10_HLT_LooseTau50_Trk30_eta2p1",&MS15ct10_HLT_LooseTau50_Trk30_eta2p1_);
MS15ct100tree_->Branch("MS15ct100_HLT_LooseTau50_Trk30_eta2p1",&MS15ct100_HLT_LooseTau50_Trk30_eta2p1_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_LooseTau50_Trk30_eta2p1",&MS15ct1000_HLT_LooseTau50_Trk30_eta2p1_);
MS40ct1tree_->Branch("MS40ct1_HLT_LooseTau50_Trk30_eta2p1",&MS40ct1_HLT_LooseTau50_Trk30_eta2p1_);
MS40ct10tree_->Branch("MS40ct10_HLT_LooseTau50_Trk30_eta2p1",&MS40ct10_HLT_LooseTau50_Trk30_eta2p1_);
MS40ct100tree_->Branch("MS40ct100_HLT_LooseTau50_Trk30_eta2p1",&MS40ct100_HLT_LooseTau50_Trk30_eta2p1_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_LooseTau50_Trk30_eta2p1",&MS40ct1000_HLT_LooseTau50_Trk30_eta2p1_);

MS7ct1tree_->Branch("MS7ct1_HLT_Mu7IP4",&MS7ct1_HLT_Mu7IP4_);
MS7ct10tree_->Branch("MS7ct10_HLT_Mu7IP4",&MS7ct10_HLT_Mu7IP4_);
MS7ct100tree_->Branch("MS7ct100_HLT_Mu7IP4",&MS7ct100_HLT_Mu7IP4_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_Mu7IP4",&MS7ct1000_HLT_Mu7IP4_);
MS15ct1tree_->Branch("MS15ct1_HLT_Mu7IP4",&MS15ct1_HLT_Mu7IP4_);
MS15ct10tree_->Branch("MS15ct10_HLT_Mu7IP4",&MS15ct10_HLT_Mu7IP4_);
MS15ct100tree_->Branch("MS15ct100_HLT_Mu7IP4",&MS15ct100_HLT_Mu7IP4_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_Mu7IP4",&MS15ct1000_HLT_Mu7IP4_);
MS40ct1tree_->Branch("MS40ct1_HLT_Mu7IP4",&MS40ct1_HLT_Mu7IP4_);
MS40ct10tree_->Branch("MS40ct10_HLT_Mu7IP4",&MS40ct10_HLT_Mu7IP4_);
MS40ct100tree_->Branch("MS40ct100_HLT_Mu7IP4",&MS40ct100_HLT_Mu7IP4_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_Mu7IP4",&MS40ct1000_HLT_Mu7IP4_);

MS7ct1tree_->Branch("MS7ct1_HLT_Mu8IP3",&MS7ct1_HLT_Mu8IP3_);
MS7ct10tree_->Branch("MS7ct10_HLT_Mu8IP3",&MS7ct10_HLT_Mu8IP3_);
MS7ct100tree_->Branch("MS7ct100_HLT_Mu8IP3",&MS7ct100_HLT_Mu8IP3_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_Mu8IP3",&MS7ct1000_HLT_Mu8IP3_);
MS15ct1tree_->Branch("MS15ct1_HLT_Mu8IP3",&MS15ct1_HLT_Mu8IP3_);
MS15ct10tree_->Branch("MS15ct10_HLT_Mu8IP3",&MS15ct10_HLT_Mu8IP3_);
MS15ct100tree_->Branch("MS15ct100_HLT_Mu8IP3",&MS15ct100_HLT_Mu8IP3_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_Mu8IP3",&MS15ct1000_HLT_Mu8IP3_);
MS40ct1tree_->Branch("MS40ct1_HLT_Mu8IP3",&MS40ct1_HLT_Mu8IP3_);
MS40ct10tree_->Branch("MS40ct10_HLT_Mu8IP3",&MS40ct10_HLT_Mu8IP3_);
MS40ct100tree_->Branch("MS40ct100_HLT_Mu8IP3",&MS40ct100_HLT_Mu8IP3_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_Mu8IP3",&MS40ct1000_HLT_Mu8IP3_);

MS7ct1tree_->Branch("MS7ct1_HLT_Mu8IP6",&MS7ct1_HLT_Mu8IP6_);
MS7ct10tree_->Branch("MS7ct10_HLT_Mu8IP6",&MS7ct10_HLT_Mu8IP6_);
MS7ct100tree_->Branch("MS7ct100_HLT_Mu8IP6",&MS7ct100_HLT_Mu8IP6_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_Mu8IP6",&MS7ct1000_HLT_Mu8IP6_);
MS15ct1tree_->Branch("MS15ct1_HLT_Mu8IP6",&MS15ct1_HLT_Mu8IP6_);
MS15ct10tree_->Branch("MS15ct10_HLT_Mu8IP6",&MS15ct10_HLT_Mu8IP6_);
MS15ct100tree_->Branch("MS15ct100_HLT_Mu8IP6",&MS15ct100_HLT_Mu8IP6_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_Mu8IP6",&MS15ct1000_HLT_Mu8IP6_);
MS40ct1tree_->Branch("MS40ct1_HLT_Mu8IP6",&MS40ct1_HLT_Mu8IP6_);
MS40ct10tree_->Branch("MS40ct10_HLT_Mu8IP6",&MS40ct10_HLT_Mu8IP6_);
MS40ct100tree_->Branch("MS40ct100_HLT_Mu8IP6",&MS40ct100_HLT_Mu8IP6_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_Mu8IP6",&MS40ct1000_HLT_Mu8IP6_);

MS7ct1tree_->Branch("MS7ct1_HLT_Mu9IP6",&MS7ct1_HLT_Mu9IP6_);
MS7ct10tree_->Branch("MS7ct10_HLT_Mu9IP6",&MS7ct10_HLT_Mu9IP6_);
MS7ct100tree_->Branch("MS7ct100_HLT_Mu9IP6",&MS7ct100_HLT_Mu9IP6_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_Mu9IP6",&MS7ct1000_HLT_Mu9IP6_);
MS15ct1tree_->Branch("MS15ct1_HLT_Mu9IP6",&MS15ct1_HLT_Mu9IP6_);
MS15ct10tree_->Branch("MS15ct10_HLT_Mu9IP6",&MS15ct10_HLT_Mu9IP6_);
MS15ct100tree_->Branch("MS15ct100_HLT_Mu9IP6",&MS15ct100_HLT_Mu9IP6_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_Mu9IP6",&MS15ct1000_HLT_Mu9IP6_);
MS40ct1tree_->Branch("MS40ct1_HLT_Mu9IP6",&MS40ct1_HLT_Mu9IP6_);
MS40ct10tree_->Branch("MS40ct10_HLT_Mu9IP6",&MS40ct10_HLT_Mu9IP6_);
MS40ct100tree_->Branch("MS40ct100_HLT_Mu9IP6",&MS40ct100_HLT_Mu9IP6_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_Mu9IP6",&MS40ct1000_HLT_Mu9IP6_);

MS7ct1tree_->Branch("MS7ct1_HLT_Mu12IP6",&MS7ct1_HLT_Mu12IP6_);
MS7ct10tree_->Branch("MS7ct10_HLT_Mu12IP6",&MS7ct10_HLT_Mu12IP6_);
MS7ct100tree_->Branch("MS7ct100_HLT_Mu12IP6",&MS7ct100_HLT_Mu12IP6_);
MS7ct1000tree_->Branch("MS7ct1000_HLT_Mu12IP6",&MS7ct1000_HLT_Mu12IP6_);
MS15ct1tree_->Branch("MS15ct1_HLT_Mu12IP6",&MS15ct1_HLT_Mu12IP6_);
MS15ct10tree_->Branch("MS15ct10_HLT_Mu12IP6",&MS15ct10_HLT_Mu12IP6_);
MS15ct100tree_->Branch("MS15ct100_HLT_Mu12IP6",&MS15ct100_HLT_Mu12IP6_);
MS15ct1000tree_->Branch("MS15ct1000_HLT_Mu12IP6",&MS15ct1000_HLT_Mu12IP6_);
MS40ct1tree_->Branch("MS40ct1_HLT_Mu12IP6",&MS40ct1_HLT_Mu12IP6_);
MS40ct10tree_->Branch("MS40ct10_HLT_Mu12IP6",&MS40ct10_HLT_Mu12IP6_);
MS40ct100tree_->Branch("MS40ct100_HLT_Mu12IP6",&MS40ct100_HLT_Mu12IP6_);
MS40ct1000tree_->Branch("MS40ct1000_HLT_Mu12IP6",&MS40ct1000_HLT_Mu12IP6_);






   if (!theChain) return 0;
   TChain          *fChain;
   TChain          *ftrigChain;
   std::cout<<"where am I?"<<std::endl;
   fChain = theChain;
   ftrigChain = trigChain;
   //fChain->SetMakeClass(1);
   //ftrigChain->SetMakeClass(1);
  Short_t bunchCrossing_;
  TString* model_=0;
  ULong64_t   HLT_Ele23Loose_;
  ULong64_t   HLT_Ele23Ele12_;
  ULong64_t   HLT_IsoTkMu22_;
  ULong64_t   HLT_Mu17Mu8_;
  ULong64_t   HLT_LooseTau50_Trk30_eta2p1_;
  ULong64_t   HLT_Mu7IP4_;
  ULong64_t   HLT_Mu8IP3_;
  ULong64_t   HLT_Mu8IP5_;
  ULong64_t   HLT_Mu8IP6_;
  ULong64_t   HLT_Mu9IP5_;
  ULong64_t   HLT_Mu9IP6_;
  ULong64_t   HLT_Mu12IP6_;
  // fChain->SetBranchAddress("model", &model);
  //fChain->Print();
  //ftrigChain->Print();
  fChain->SetBranchAddress("model", &model_);
  //fChain->SetBranchAddress("bunchCrossing", &bunchCrossing_);
  ftrigChain->SetBranchAddress("HLT_Ele23Loose",       &HLT_Ele23Loose_) ;
  ftrigChain->SetBranchAddress("HLT_Ele23Ele12",       &HLT_Ele23Ele12_) ;

  ftrigChain->SetBranchAddress("HLT_IsoTkMu22",        &HLT_IsoTkMu22_) ;
  ftrigChain->SetBranchAddress("HLT_Mu17Mu8"  ,        &HLT_Mu17Mu8_)   ;
  ftrigChain->SetBranchAddress("HLT_LooseTau50_Trk30_eta2p1",       &HLT_LooseTau50_Trk30_eta2p1_) ;
  ftrigChain->SetBranchAddress("HLT_Mu7IP4",       &HLT_Mu7IP4_) ;
  ftrigChain->SetBranchAddress("HLT_Mu8IP3",       &HLT_Mu8IP3_) ;
  ftrigChain->SetBranchAddress("HLT_Mu8IP6",       &HLT_Mu8IP6_) ;
  ftrigChain->SetBranchAddress("HLT_Mu9IP5",       &HLT_Mu9IP5_) ;
  ftrigChain->SetBranchAddress("HLT_Mu9IP6",       &HLT_Mu9IP6_) ;
  ftrigChain->SetBranchAddress("HLT_Mu12IP6",       &HLT_Mu12IP6_) ;

 Long64_t nb;
 Long64_t nbytes;
 Long64_t trignb;
 Long64_t trignbytes;
 Long64_t nentries = fChain->GetEntries();
 //int nentries = fChain->GetEntries();
  std::cout<<nentries<<std::endl;
 for (Long64_t jentry=0; jentry<nentries;jentry++) {
   //std::cout<<"where am I?"<<std::endl;
  nb = fChain->GetEntry(jentry);
   //std::cout<<"where am I?"<<std::endl;
   //std::cout<<*model_<<std::endl;
  trignb = ftrigChain->GetEntry(jentry);
  //if(HLT_Ele23Ele12_>0) std::cout<<HLT_Ele23Ele12_<<std::endl;
  if (jentry%10000 == 0){ std::cout << " entry " << jentry << std::endl; }
 float tempTrackMass;
 if(model_->Contains("MS-7_ctauS-1_"))
 { 
 MS7ct1_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS7ct1_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS7ct1_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS7ct1_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS7ct1_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS7ct1_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS7ct1_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS7ct1_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS7ct1_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS7ct1_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS7ct1tree_->Fill(); 
 } 
 else if(model_->Contains("MS-7_ctauS-10_"))
 { 
 MS7ct10_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS7ct10_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS7ct10_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS7ct10_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS7ct10_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS7ct10_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS7ct10_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS7ct10_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS7ct10_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS7ct10_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS7ct10tree_->Fill(); 
 } 
 else if(model_->Contains("MS-7_ctauS-100_"))
 { 
 MS7ct100_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS7ct100_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS7ct100_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS7ct100_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS7ct100_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS7ct100_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS7ct100_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS7ct100_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS7ct100_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS7ct100_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS7ct100tree_->Fill(); 
 } 
 else if(model_->Contains("MS-7_ctauS-1000_"))
 { 
 MS7ct1000_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS7ct1000_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS7ct1000_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS7ct1000_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS7ct1000_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS7ct1000_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS7ct1000_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS7ct1000_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS7ct1000_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS7ct1000_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS7ct1000tree_->Fill(); 
 } 

 else if(model_->Contains("MS-15_ctauS-1_"))
 { 
 MS15ct1_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS15ct1_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS15ct1_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS15ct1_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS15ct1_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS15ct1_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS15ct1_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS15ct1_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS15ct1_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS15ct1_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS15ct1tree_->Fill(); 
 } 
 else if(model_->Contains("MS-15_ctauS-10_"))
 { 
 MS15ct10_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS15ct10_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS15ct10_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS15ct10_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS15ct10_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS15ct10_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS15ct10_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS15ct10_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS15ct10_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS15ct10_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS15ct10tree_->Fill(); 
 } 
 else if(model_->Contains("MS-15_ctauS-100_"))
 { 
 MS15ct100_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS15ct100_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS15ct100_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS15ct100_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS15ct100_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS15ct100_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS15ct100_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS15ct100_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS15ct100_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS15ct100_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS15ct100tree_->Fill(); 
 } 
 else if(model_->Contains("MS-15_ctauS-1000_"))
 { 
 MS15ct1000_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS15ct1000_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS15ct1000_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS15ct1000_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS15ct1000_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS15ct1000_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS15ct1000_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS15ct1000_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS15ct1000_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS15ct1000_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS15ct1000tree_->Fill(); 
 } 

 else if(model_->Contains("MS-40_ctauS-1_"))
 { 
 MS40ct1_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS40ct1_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS40ct1_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS40ct1_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS40ct1_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS40ct1_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS40ct1_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS40ct1_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS40ct1_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS40ct1_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS40ct1tree_->Fill(); 
 } 
 else if(model_->Contains("MS-40_ctauS-10_"))
 { 
 MS40ct10_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS40ct10_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS40ct10_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS40ct10_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS40ct10_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS40ct10_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS40ct10_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS40ct10_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS40ct10_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS40ct10_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS40ct10tree_->Fill(); 
 } 
 else if(model_->Contains("MS-40_ctauS-100_"))
 { 
 MS40ct100_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS40ct100_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS40ct100_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS40ct100_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS40ct100_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS40ct100_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS40ct100_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS40ct100_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS40ct100_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS40ct100_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS40ct100tree_->Fill(); 
 } 
 else if(model_->Contains("MS-40_ctauS-1000_"))
 { 
 MS40ct1000_HLT_Ele23Ele12_ = HLT_Ele23Ele12_;
 MS40ct1000_HLT_Ele23Loose_ = HLT_Ele23Loose_;
 MS40ct1000_HLT_IsoTkMu22_ = HLT_IsoTkMu22_;
 MS40ct1000_HLT_LooseTau50_Trk30_eta2p1_ = HLT_LooseTau50_Trk30_eta2p1_;
 MS40ct1000_HLT_Mu17Mu8_ = HLT_Mu17Mu8_;
 MS40ct1000_HLT_Mu8IP3_ = HLT_Mu8IP3_;
 MS40ct1000_HLT_Mu8IP6_ = HLT_Mu8IP6_;
 MS40ct1000_HLT_Mu9IP6_ = HLT_Mu9IP6_;
 MS40ct1000_HLT_Mu12IP6_ = HLT_Mu12IP6_;
 MS40ct1000_HLT_Mu7IP4_ = HLT_Mu7IP4_;
 MS40ct1000tree_->Fill(); 
 } 
 else{}









}

   std::cout<<"where am I?"<<std::endl;
 TFile* newfile = new TFile(outfilename+".root", "RECREATE");
 MS7ct1tree_->Write();
 MS7ct10tree_->Write();
 MS7ct100tree_->Write();
 MS7ct1000tree_->Write();
 MS15ct1tree_->Write();
 MS15ct10tree_->Write();
 MS15ct100tree_->Write();
 MS15ct1000tree_->Write();
 MS40ct1tree_->Write();
 MS40ct10tree_->Write();
 MS40ct100tree_->Write();
 MS40ct1000tree_->Write();


 return 0;
}
