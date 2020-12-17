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

void Sig_table_stackedRegion(TString region, Bool_t dolog, Bool_t HIP, Bool_t useEOS, TString description)
{

// // Draw signal as lines
Bool_t drawSignal = kTRUE; //kTRUE; //kFALSE
//Bool_t drawWHSignal = kTRUE;
// Bool_t drawRatio = kTRUE;

 // Setup running configuration: IO, naming, SFs, ..
 /////////////////////////////////////////////////////

 bool drawData = true;
 bool useAlt = false; 
 bool doUncPlots = true;

 TString outpath = TString("temproot/");
 TString inpath  = TString("temproot/");

 //inpath = inpath+aversion+"/";

 TString extraname = "";

 // lumi scaling by era
 Float_t MCSF = 1.;
 //Float_t lumifb = 58670. ;
 Float_t lumifb = 16150. ;
 MCSF = (lumifb)/20000.; 
 
 //TString extraname = "";
 if(dolog){
  extraname+="_log";
  //outpath = outpath+"log/";
 }

 TString mdcommand = (TString)"mkdir -p "+outpath.Data();
 const int dir_err = system(mdcommand);
 TString mdcommandtable = (TString)"mkdir -p "+outpath.Data()+"tables/";
 const int dir_err2 = system(mdcommandtable);

 std::vector<string> MSbins;
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-10"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-100"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-55_ctauS-1000"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-10"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-100"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-40_ctauS-1000"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-100"); 
 MSbins.push_back("ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-1000"); 
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
 //MSbins.push_back("Sig_MS55ct1"); 
 //MSbins.push_back("Sig_MS55ct10"); 
 //MSbins.push_back("Sig_MS55ct100"); 
 //MSbins.push_back("Sig_MS55ct1000"); 
 //MSbins.push_back("Sig_MS40ct1"); 
 //MSbins.push_back("Sig_MS40ct10"); 
 //MSbins.push_back("Sig_MS40ct100"); 
 //MSbins.push_back("Sig_MS40ct1000"); 
 //MSbins.push_back("Sig_MS15ct1"); 
 //MSbins.push_back("Sig_MS15ct10"); 
 //MSbins.push_back("Sig_MS15ct100"); 
 //MSbins.push_back("Sig_MS15ct1000"); 
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
  for(unsigned int tt=0; tt<loopEnd; ++tt){
    TString uncbin = uncbins[tt];
     TString logname = "temproot/Ntrack"+region+uncbin+"_full_text"; 
      outfulltable = fopen (logname+".tex","w");
       //fprintf (outfulltable, "Signal Point, 0-Tag central/up/down, 1-Tag central/up/down, 2-Tag central/up/down:\\\\\n") ; 
       if(region.Contains("DY")){fprintf (outfulltable, "Signal Point, LowZ 0-Tag up/down 1-Tag up/down 2-Tag up/down") ; 
       fprintf (outfulltable, "                                                 \n") ;} 
       else{ 
       fprintf (outfulltable, "                                                 \n") ; 
       fprintf (outfulltable, " \\begin{table}\n") ;
       fprintf (outfulltable, " \\tiny\n") ;
       fprintf (outfulltable, " \\begin{adjustbox}{width=.5\\textwidth}\n") ;
       fprintf (outfulltable, " \\centering\n") ;
       fprintf (outfulltable, " \\begin{tabular}{|p{3cm}|p{1cm}|p{2cm}|p{2cm}|p{2cm}|}    \n") ;
       fprintf (outfulltable, "          \\hline                                  \n") ;  
       fprintf (outfulltable, "        HighZ&Tag & Signal&DY&Punzi             \\\\") ; 
       fprintf (outfulltable, "                                           \n") ;  
       fprintf (outfulltable, "          \\hline                                  \n") ;  
       fprintf (outfulltable, "                                                 \n") ; } 
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
  for(unsigned int j=0; j<variables.size(); ++j){
   TString variable = variables[j];

    //Override drawData for nTag signal region
 file_ZH_NoUnc                    = TFile::Open( inpath +"new"+region+"_"+MSsample+"_Nov20Ntrack.root"                 ) ;
 file_ggZH_NoUnc                    = TFile::Open( inpath +"new"+region+"_gg"+MSsample+"_Nov20Ntrack.root"                 ) ;
 file_DY                    = TFile::Open( inpath +"new"+region+"_DYJetsToLL_M-50_Nov20Ntrack.root"                 ) ;

     TString varname = region+"_"+variable;

     printf("plotting  h_%s \n",varname.Data());

     h_ZH_NoUnc       = (TH1F*)file_ZH_NoUnc    ->Get("h_"+varname)->Clone( "ZH_NoUnc" ) ;
     h_ggZH_NoUnc       = (TH1F*)file_ggZH_NoUnc    ->Get("h_"+varname)->Clone( "ZH_NoUnc" ) ;
     h_DY       = (TH1F*)file_DY    ->Get("h_"+varname )->Clone( "ZH_NoUnc" ) ;
	cout<<"here"<<endl;

    Float_t Sig_NoUnc_tag0 = h_ZH_NoUnc->GetBinContent(1)+h_ggZH_NoUnc->GetBinContent(1);
    Float_t DY_tag0 = h_DY->GetBinContent(1);
    Float_t Sig_NoUnc_tag1 = h_ZH_NoUnc->GetBinContent(2)+h_ggZH_NoUnc->GetBinContent(2);
    Float_t DY_tag1 = h_DY->GetBinContent(2);
    Float_t Sig_NoUnc_tag2 = h_ZH_NoUnc->GetBinContent(3)+h_ggZH_NoUnc->GetBinContent(3);
    Float_t DY_tag2 = h_DY->GetBinContent(3);
    Float_t punzi0 = Sig_NoUnc_tag0/sqrt(2.5+DY_tag0); 
    Float_t punzi1 = Sig_NoUnc_tag1/sqrt(2.5+DY_tag1); 
    Float_t punzi2 = Sig_NoUnc_tag2/sqrt(2.5+DY_tag2); 
  
// save histograms into single root file
	std::replace( mssample.begin(), mssample.end(), '_', '-');	
       fprintf (outfulltable, "%s/DY & Tag0 & %8.6f &%8.6f &%8.6f \\\\\n",mssample.c_str(), Sig_NoUnc_tag0,DY_tag0,punzi0) ; 
       fprintf (outfulltable, "        & Tag1 & %8.6f &%8.6f &%8.6f \\\\\n", Sig_NoUnc_tag1,DY_tag1,punzi1) ; 
       fprintf (outfulltable, "        & Tag2 & %8.6f &%8.6f &%8.6f \\\\\n", Sig_NoUnc_tag2,DY_tag2,punzi2) ; 

   } 
  }
       fprintf (outfulltable, "          \\hline                                  \n") ;  
       fprintf (outfulltable, " \\end{tabular}   \n") ;
       fprintf (outfulltable, " \\end{adjustbox}\n") ;
       fprintf (outfulltable, " \\end{table}\n") ;
      fclose (outfulltable);
}  
}
