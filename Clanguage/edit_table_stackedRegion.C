#include <iostream>
#include "TString.h"
#include "TH1F.h"
#include "TCanvas.h"
#include "THStack.h"
#include "TLegend.h"
#include "TPad.h"
#include "TStyle.h"
#include "TText.h"
#include "TFile.h"
#include <stdio.h>
#include <cstdlib> /* mkdir */

#include <stdlib.h>     /* getenv */

void edit_table_stackedRegion(TString region, Bool_t dolog,  TString description, TString year)
{
TString Year= year;
// // Draw signal as lines
Bool_t drawSignal = kTRUE; //kTRUE; //kFALSE
//Bool_t drawWHSignal = kTRUE;
// Bool_t drawRatio = kTRUE;

 // Setup running configuration: IO, naming, SFs, ..
 /////////////////////////////////////////////////////

 bool drawData = true;
 bool useAlt = false; 
 bool doUncPlots = true;

 TString inpath  = TString("temproot/2016/");
 if(Year.Contains("2016")){
 inpath  = TString("temproot/2016/");
}
 else if(Year.Contains("2017")){
 inpath  = TString("temproot/2017/");
}
 else if(Year.Contains("2018")){
 inpath  = TString("temproot/2018/");
}
 else{
 inpath  = TString("temproot/");
}
 //inpath = inpath+aversion+"/";

 TString extraname = "";

 // lumi scaling by era
 Float_t MCSF = 1.;
 Float_t lumifb = 59403. ;
// Float_t lumifb = 16150. ;
 MCSF = (lumifb)/20000.; 
 
 //TString extraname = "";
 if(dolog){
  extraname+="_log";
  //outpath = outpath+"log/";
 }

 TString mdcommand = (TString)"mkdir -p Results";
 const int dir_err = system(mdcommand);

 std::vector<string> MSbins;
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100"); 
 //MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100"); 
 //MSbins.push_back("ggZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000"); 
 //MSbins.push_back("DY"); 
 MSbins.push_back("Sig_MS-55_ctauS-1"); 
 MSbins.push_back("Sig_MS-55_ctauS-10"); 
 MSbins.push_back("Sig_MS-55_ctauS-100"); 
 MSbins.push_back("Sig_MS-55_ctauS-1000"); 
 MSbins.push_back("Sig_MS-40_ctauS-1"); 
 MSbins.push_back("Sig_MS-40_ctauS-10"); 
 MSbins.push_back("Sig_MS-40_ctauS-100"); 
 MSbins.push_back("Sig_MS-40_ctauS-1000"); 
 MSbins.push_back("Sig_MS-15_ctauS-1"); 
 MSbins.push_back("Sig_MS-15_ctauS-10"); 
 MSbins.push_back("Sig_MS-15_ctauS-100"); 
 MSbins.push_back("Sig_MS-15_ctauS-1000"); 
 std::vector<TString> uncbins;
 uncbins.clear();
//// uncbins.push_back("_ESFUp"       );    
 uncbins.push_back("_JES"     );    

 int loopEnd;
 if (doUncPlots) loopEnd=uncbins.size(); else loopEnd=1;
//if(drawSignal){extraname+="_wsig";}
//if(drawWHSignal){extraname+="_wWHsig";}
// variables to plot
 std::vector<TString> variables;
 variables.clear();

variables.push_back("nSelectedAODCaloJetTag");
variables.push_back("nSelectedAODCaloJetTagSB1");
variables.push_back("nSelectedAODCaloJetTagSB2");
variables.push_back("nSelectedAODCaloJetTagSB3");
variables.push_back("nSelectedAODCaloJetTagSB4");
variables.push_back("nSelectedAODCaloJetTagSB5");
variables.push_back("nSelectedAODCaloJetTagSB6");
variables.push_back("nSelectedAODCaloJetTagSB7");

 // canvas and text attributes
 int canx = 1100;
 int cany = 900;
 float lmarg = 0.12;
 float rmarg = 0.05;
 if(drawData) cany = 1200;

 TCanvas* canvas = new TCanvas("canvas","canvas",canx,cany); 

 gStyle->SetOptStat(0);
 gPad->SetLogy(dolog);
 gPad->SetTickx();
 gPad->SetTicky();
 gStyle->SetLineWidth(3);
 gStyle->SetPalette(kBird);

 canvas->Clear();
 canvas->cd();


 // initialize histogram files
 TFile* file_DY                               ;
 TFile* file_ZH_NoUnc                                ;
 TFile* file_EleZH_NoUnc                                ;
 TFile* file_ZH_JECUp                                ;
 TFile* file_ZH_JECDown                                ;
 TFile* file_ggZH_NoUnc                                ;
 TFile* file_ggZH_JECUp                                ;
 TFile* file_ggZH_JECDown                                ;

 // initialize histos
 TH1F* h_DY      ;
 TH1F* h_ZH_NoUnc      ;
 TH1F* h_ZH_JECUp      ;
 TH1F* h_ZH_JECDown      ;
 TH1F* h_EleZH_NoUnc      ;
 TH1F* h_EleZH_JECUp      ;
 TH1F* h_EleZH_JECDown      ;
 TH1F* h_ggZH_NoUnc      ;
 TH1F* h_ggZH_JECUp      ;
 TH1F* h_ggZH_JECDown      ;
 TH1F* h_ratio ;
 TH1F* h_ratio2 ;
 TH1F* h_ratiostaterr ;


 // (combined) histos to be made
 TH1F* h_bkgtotal ;
 TH1F* h_Sig_NoUnc  ;
 TH1F* h_Sig_JECUp  ;
 TH1F* h_Sig_JECDown  ;
      FILE * outfulltable;
  //for(unsigned int tt=0; tt<loopEnd; ++tt){
  for(unsigned int j=0; j<variables.size(); ++j){
   TString variable = variables[j];
    TString uncbin = uncbins[0];
      TString logname = "Results/"+variable+"_"+region+uncbin+"_full_text"; 
	if(Year.Contains("2016")){
      logname = "Results/2016/"+variable+"_"+region+uncbin+"_full_text"; 
}
	else if(Year.Contains("2017")){
     logname = "Results/2017/"+variable+"_"+region+uncbin+"_full_text"; 
	}
	else if(Year.Contains("2018")){
      logname = "Results/2018/"+variable+"_"+region+uncbin+"_full_text"; 
	}
	else{
      logname = "Results/"+variable+"_"+region+uncbin+"_full_text"; 
	}
      outfulltable = fopen (logname+".txt","w");
       //fprintf (outfulltable, "Signal Point, 0-Tag central/up/down, 1-Tag central/up/down, 2-Tag central/up/down:\\\\\n") ; 
       if(region.Contains("DY")){fprintf (outfulltable, "Signal Point, LowZ 0-Tag up/down 1-Tag up/down 2-Tag up/down") ; 
       fprintf (outfulltable, "                                                 \n") ;} 
       else{ 
       fprintf (outfulltable, "Signal Point, HighZ 0-Tag central/up/down, 1-Tag central/up/down, 2-Tag central/up/down") ;   
       fprintf (outfulltable, "                                                 \n") ; 
       fprintf (outfulltable, "                                                 \n") ;} 
std::cout<<"where"<<std::endl; 
for(unsigned int k=0; k<MSbins.size(); ++k){
 //file_Sig                    = TFile::Open( inpath + "Sig_MS-55_ctauS-100_"+region+".root"                 ) ;
 TString MSsample = MSbins[k];
 string mssample = MSbins[k];
 mssample = mssample.substr(mssample.find("MS-"),mssample.size());
 // load histogram files
 //file_DY10to50                = TFile::Open( inpath + "DYJetsToLL_M-10to50_"+region+"_histograms.root"             ) ; 
cout<<"where"<<endl;

 // Start looping over variables, systematic uncertainty bins, make plots / tables / root files

    //Override drawData for nTag signal region
 file_ZH_NoUnc                    = TFile::Open( inpath+MSsample+"_TwoMuZH_histograms.root"                 ) ;
 file_EleZH_NoUnc                    = TFile::Open( inpath+MSsample+"_TwoEleZH_histograms.root"                 ) ;

     //TString varname = region+"_"+variable;
     TString varname = variable;

     printf("plotting  h_%s \n",varname.Data());

     h_ZH_NoUnc       = (TH1F*)file_ZH_NoUnc    ->Get("h_TwoMuZH_"+varname)->Clone( "ZH_NoUnc" ) ;
     h_ZH_JECUp       = (TH1F*)file_ZH_NoUnc    ->Get("h_TwoMuZH_"+varname+"_JESUp")->Clone( "ZH_JESUp" ) ;
     h_ZH_JECDown       = (TH1F*)file_ZH_NoUnc  ->Get("h_TwoMuZH_"+varname+"_JESDown")->Clone( "ZH_JESDown" ) ;
     h_EleZH_NoUnc       = (TH1F*)file_EleZH_NoUnc    ->Get("h_TwoEleZH_"+varname)->Clone( "EleZH_NoUnc" ) ;
     h_EleZH_JECUp       = (TH1F*)file_EleZH_NoUnc    ->Get("h_TwoEleZH_"+varname+"_JESUp")->Clone( "EleZH_JESUp" ) ;
     h_EleZH_JECDown       = (TH1F*)file_EleZH_NoUnc  ->Get("h_TwoEleZH_"+varname+"_JESDown")->Clone( "EleZH_JESDown" ) ;
	cout<<"here"<<endl;
	h_ZH_NoUnc->Add(h_EleZH_NoUnc);
	h_ZH_JECUp->Add(h_EleZH_JECUp);
	h_ZH_JECDown->Add(h_EleZH_JECDown);
	Float_t Tag0No = h_ZH_NoUnc->GetBinContent(1);  
	Float_t Tag0JECUp = h_ZH_JECUp->GetBinContent(1);  
	Float_t Tag0JECDown = h_ZH_JECDown->GetBinContent(1);  
	Float_t Tag1No = h_ZH_NoUnc->GetBinContent(2);  
	Float_t Tag1JECUp = h_ZH_JECUp->GetBinContent(2);  
	Float_t Tag1JECDown = h_ZH_JECDown->GetBinContent(2);  
	Float_t Tag2No = h_ZH_NoUnc->GetBinContent(3);  
	Float_t Tag2JECUp = h_ZH_JECUp->GetBinContent(3);  
	Float_t Tag2JECDown = h_ZH_JECDown->GetBinContent(3);  
// save histograms into single root file
	std::replace( mssample.begin(), mssample.end(), '_', '-');	
       fprintf (outfulltable, "%s  %8.6f,%8.6f,%8.6f  %8.6f,%8.6f,%8.6f     %8.6f,%8.6f,%8.6f",mssample.c_str(), Tag0No,Tag0JECUp,Tag0JECDown, Tag1No,Tag1JECUp,Tag1JECDown, Tag2No,Tag2JECUp,Tag2JECDown) ; 
       fprintf (outfulltable, "                                                 \n") ; 

    
  }
      fclose (outfulltable);
}  
}
