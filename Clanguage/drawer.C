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

 // for getting command line options
 // s - sample name
 // i - inpath
 // o - outpath
 // n - nfiles
 /*char *sample = NULL;
 char *inpath = (char*)"../lists";
 char *outpath = (char*)"../roots";
 char *nfiles = (char*)"-1";
 int index;
 int s;


 while ((s = getopt (argc, argv, "s:i:o:n")) != -1)
  switch (s)
   {
   case 'n':
    nfiles = optarg;
    break;
   case 'o':
    outpath = optarg;
    break;
   case 'i':
    inpath = optarg;
    break;
   case 's':
    sample = optarg;
    break;
   default:
    abort ();
   }

// for (index = optind; index < argc; index++)
//   std::cout << "Non-option argument " << argv[index] << std::endl;
*/
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

 TChain *theChain = new TChain("lldjNtuple/EventTree");
 theChain->Reset();

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
   std::cout << " Inputfile: " << Tinputline << std::endl;
  }



  inputline_dump.push_back(inputline);
 } // while( std::getline(inputfile, inputline) )
 inputfile.close();


 // make the analyzer, init some stuff
 //analyzer_loop analyzer;
 //analyzer.setConfiguration();

 //TString outfilenamebase = outfilename;
 //analyzer.Init(theChain, isMC, makelog, Tsample, unccategory);
 //////////////////////////////////////////////////////////////////
   if (!theChain) return 0;
   TChain          *fChain;
   std::cout<<"where am I?"<<std::endl;
   //fChain->Reset();
   fChain = theChain;
   //fCurrent = -1;
   fChain->SetMakeClass(1);
 
   std::vector<float>   *AODCaloJetTrackMass = 0; 
   //fChain->SetBranchAddress("AODCaloJetAlphaMax", &AODCaloJetTrackMass);
   fChain->SetBranchAddress("AODCaloJetTrackMass", &AODCaloJetTrackMass);
	TH1F* hVar = new TH1F("Variable","Variable",98, 0.2, 10);
 Long64_t nb;
 Long64_t nbytes;
 Long64_t nentries = fChain->GetEntries();
 //int nentries = fChain->GetEntries();
  std::cout<<nentries<<std::endl;
 for (Long64_t jentry=0; jentry<nentries;jentry++) {
   //std::cout<<"where am I?"<<std::endl;
  //Long64_t ientry = LoadTree(jentry);
  //if (ientry < 0) break;
  nb = fChain->GetEntry(jentry);
  if (jentry%10000 == 0){ std::cout << " entry " << jentry << std::endl; }
 float tempTrackMass;
 for(int i = 0; i < AODCaloJetTrackMass->size(); i++)
 { tempTrackMass = 0;
   tempTrackMass = AODCaloJetTrackMass->at(i);
    hVar->Fill(tempTrackMass);
 } // loop over jets
 }
   std::cout<<"where am I?"<<std::endl;
 TFile* newfile = new TFile(outfilename+".root", "RECREATE");
  hVar->Write();
 return 0;
}
