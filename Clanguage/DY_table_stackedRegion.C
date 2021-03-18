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

void DY_table_stackedRegion(TString region, Bool_t dolog,  TString description, TString year)
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

 TString mdcommand = (TString)"mkdir -p DYResults";
 const int dir_err = system(mdcommand);

 std::vector<string> MSbins;
 MSbins.push_back("DYJetsToLL_M-50"); 
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

//variables.push_back("nSelectedAODCaloJetTagSB3");
//variables.push_back("nSelectedAODCaloJetTagSB5");
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
 TFile* file_DY_NoUnc                                ;
 TFile* file_EleDY_NoUnc                                ;
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
 TH1F* h_DY_NoUnc      ;
 TH1F* h_DY_JECUp      ;
 TH1F* h_DY_JECDown      ;
 TH1F* h_EleDY_NoUnc      ;
 TH1F* h_EleDY_JECUp      ;
 TH1F* h_EleDY_JECDown      ;
 TH1F* h_ggZH_NoUnc      ;
 TH1F* h_ggZH_JECUp      ;
 TH1F* h_ggZH_JECDown      ;
 TH1F* h_TF_NoUnc ;
 TH1F* h_TF_UU ;
 TH1F* h_TF_DD ;
 TH1F* h_TF_UD ;
 TH1F* h_TF_DU ;
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
      TString logname = "DYResults/DYTF_"+variable+"_"+region+uncbin+"_full_text"; 
	if(Year.Contains("2016")){
      logname = "DYResults/2016/DYTF_"+variable+"_"+region+uncbin+"_full_text"; 
}
	else if(Year.Contains("2017")){
     logname = "DYResults/2017/DYTF_"+variable+"_"+region+uncbin+"_full_text"; 
	}
	else if(Year.Contains("2018")){
      logname = "DYResults/2018/DYTF_"+variable+"_"+region+uncbin+"_full_text"; 
	}
	else{
      logname = "DYResults/DYTF_"+variable+"_"+region+uncbin+"_full_text"; 
	}
      outfulltable = fopen (logname+".txt","w");
       //fprintf (outfulltable, "Signal Point, 0-Tag central/up/down, 1-Tag central/up/down, 2-Tag central/up/down:\\\\\n") ; 
       if(region.Contains("DY")){fprintf (outfulltable, "Signal Point, LowZ 0-Tag up/down 1-Tag up/down 2-Tag up/down") ; 
       fprintf (outfulltable, "                                                 \n") ;} 
       else{ 
       fprintf (outfulltable, "DYJetsToLL_M-50, HighZ 0-Tag central/up/down, 1-Tag central/up/down, 2-Tag central/up/down") ;   
       fprintf (outfulltable, "                                                 \n") ; 
       fprintf (outfulltable, "DYJetsToLL_M-50, LowZ 0-Tag central/up/down, 1-Tag central/up/down , 1-Tag central/up/down ") ;   
       fprintf (outfulltable, "                                                 \n") ; 
       fprintf (outfulltable, "DYJetsToLL_M-50, TF 0-Tag central/upup/downdown/upcentral/downcentral, 1-Tag central/upup/downdown/upcentral/downcentral ,2-Tag central/upup/downdown/upcentral/downcentral      ") ;   
       fprintf (outfulltable, "                                                 \n") ; 
       fprintf (outfulltable, "                                                 \n") ;} 
std::cout<<"where"<<std::endl; 
for(unsigned int k=0; k<MSbins.size(); ++k){
 //file_Sig                    = TFile::Open( inpath + "Sig_MS-55_ctauS-100_"+region+".root"                 ) ;
 TString MSsample = MSbins[k];
 string mssample = MSbins[k];
 //mssample = mssample.substr(mssample.find("MS-"),mssample.size());
 // load histogram files
 //file_DY10to50                = TFile::Open( inpath + "DYJetsToLL_M-10to50_"+region+"_histograms.root"             ) ; 
cout<<"where"<<endl;

 // Start looping over variables, systematic uncertainty bins, make plots / tables / root files

    //Override drawData for nTag signal region
 file_ZH_NoUnc                    = TFile::Open( inpath+MSsample+"_TwoMuZH_histograms.root"                 ) ;
 file_EleZH_NoUnc                    = TFile::Open( inpath+MSsample+"_TwoEleZH_histograms.root"                 ) ;

     //TString varname = region+"_"+variable;
     TString varname = variable;


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
    //Override drawData for nTag signal region
 file_DY_NoUnc                    = TFile::Open( inpath+MSsample+"_TwoMuDY_histograms.root"                 ) ;
 file_EleDY_NoUnc                    = TFile::Open( inpath+MSsample+"_TwoEleDY_histograms.root"                 ) ;



     h_DY_NoUnc       = (TH1F*)file_DY_NoUnc    ->Get("h_TwoMuDY_"+varname)->Clone( "DY_NoUnc" ) ;
     h_DY_JECUp       = (TH1F*)file_DY_NoUnc    ->Get("h_TwoMuDY_"+varname+"_JESUp")->Clone( "DY_JESUp" ) ;
     h_DY_JECDown       = (TH1F*)file_DY_NoUnc  ->Get("h_TwoMuDY_"+varname+"_JESDown")->Clone( "DY_JESDown" ) ;
     h_EleDY_NoUnc       = (TH1F*)file_EleDY_NoUnc    ->Get("h_TwoEleDY_"+varname)->Clone( "EleDY_NoUnc" ) ;
     h_EleDY_JECUp       = (TH1F*)file_EleDY_NoUnc    ->Get("h_TwoEleDY_"+varname+"_JESUp")->Clone( "EleDY_JESUp" ) ;
     h_EleDY_JECDown       = (TH1F*)file_EleDY_NoUnc  ->Get("h_TwoEleDY_"+varname+"_JESDown")->Clone( "EleDY_JESDown" ) ;
	cout<<"here"<<endl;
	h_DY_NoUnc->Add(h_EleDY_NoUnc);
	h_DY_JECUp->Add(h_EleDY_JECUp);
	h_DY_JECDown->Add(h_EleDY_JECDown);
    //Override drawData for nTag signal region

     h_TF_NoUnc = (TH1F*)h_ZH_NoUnc->Clone("TF_NoUnc");
     h_TF_NoUnc->Divide(h_DY_NoUnc);
     h_TF_UU = (TH1F*)h_ZH_JECUp->Clone("TF_UU");
     h_TF_UU->Divide(h_DY_JECUp);
     h_TF_DD = (TH1F*)h_ZH_JECDown->Clone("TF_DD");
     h_TF_DD->Divide(h_DY_JECDown);
     h_TF_UD = (TH1F*)h_ZH_JECUp->Clone("TF_UD");
     h_TF_UD->Divide(h_DY_NoUnc);
     h_TF_DU = (TH1F*)h_ZH_JECDown->Clone("TF_DU");
     h_TF_DU->Divide(h_DY_NoUnc);
	cout<<"here"<<endl;

	Float_t Tag0No = h_ZH_NoUnc->GetBinContent(1);  
	Float_t Tag0JECUp = h_ZH_JECUp->GetBinContent(1);  
	Float_t Tag0JECDown = h_ZH_JECDown->GetBinContent(1);  
	Float_t Tag1No = h_ZH_NoUnc->GetBinContent(2);  
	Float_t Tag1JECUp = h_ZH_JECUp->GetBinContent(2);  
	Float_t Tag1JECDown = h_ZH_JECDown->GetBinContent(2);  
	Float_t Tag2No = h_ZH_NoUnc->GetBinContent(3);  
	Float_t Tag2JECUp = h_ZH_JECUp->GetBinContent(3);  
	Float_t Tag2JECDown = h_ZH_JECDown->GetBinContent(3);  
	Float_t DYTag0No = h_DY_NoUnc->GetBinContent(1);  
	Float_t DYTag0JECUp = h_DY_JECUp->GetBinContent(1);  
	Float_t DYTag0JECDown = h_DY_JECDown->GetBinContent(1);  
	Float_t DYTag1No = h_DY_NoUnc->GetBinContent(2);  
	Float_t DYTag1JECUp = h_DY_JECUp->GetBinContent(2);  
	Float_t DYTag1JECDown = h_DY_JECDown->GetBinContent(2);  
	Float_t DYTag2No = h_DY_NoUnc->GetBinContent(3);  
	Float_t DYTag2JECUp = h_DY_JECUp->GetBinContent(3);  
	Float_t DYTag2JECDown = h_DY_JECDown->GetBinContent(3);  


	Float_t TF0No = h_TF_NoUnc->GetBinContent(1);  
	Float_t TF0UU = h_TF_UU->GetBinContent(1);  
	Float_t TF0DD = h_TF_DD->GetBinContent(1);  
	Float_t TF0UD = h_TF_UD->GetBinContent(1);  
	Float_t TF0DU = h_TF_DU->GetBinContent(1);  
	Float_t TF1No = h_TF_NoUnc->GetBinContent(2);  
	Float_t TF1UU = h_TF_UU->GetBinContent(2);  
	Float_t TF1DD = h_TF_DD->GetBinContent(2);  
	Float_t TF1UD = h_TF_UD->GetBinContent(2);  
	Float_t TF1DU = h_TF_DU->GetBinContent(2);  
	Float_t TF2No = h_TF_NoUnc->GetBinContent(3);  
	Float_t TF2UU = h_TF_UU->GetBinContent(3);  
	Float_t TF2DD = h_TF_DD->GetBinContent(3);  
	Float_t TF2UD = h_TF_UD->GetBinContent(3);  
	Float_t TF2DU = h_TF_DU->GetBinContent(3);  
	TF0UU = (TF0UU-TF0No)/TF0No;
	TF0DD = (TF0DD-TF0No)/TF0No;
	TF0UD = (TF0UD-TF0No)/TF0No;
	TF0DU = (TF0DU-TF0No)/TF0No;
	TF1UU = (TF1UU-TF1No)/TF1No;
	TF1DD = (TF1DD-TF1No)/TF1No;
	TF1UD = (TF1UD-TF1No)/TF1No;
	TF1DU = (TF1DU-TF1No)/TF1No;
	TF2UU = (TF2UU-TF2No)/TF2No;
	TF2DD = (TF2DD-TF2No)/TF2No;
	TF2UD = (TF2UD-TF2No)/TF2No;
	TF2DU = (TF2DU-TF2No)/TF2No;

	



// save histograms into single root file
	std::replace( mssample.begin(), mssample.end(), '_', '-');	
       fprintf (outfulltable, "HighZ  %8.6f,%8.6f,%8.6f  %8.6f,%8.6f,%8.6f   %8.6f,%8.6f,%8.6f ", Tag0No,Tag0JECUp,Tag0JECDown, Tag1No,Tag1JECUp,Tag1JECDown , Tag2No,Tag2JECUp,Tag2JECDown        ) ; 
       fprintf (outfulltable, "                                                 \n") ; 
       fprintf (outfulltable, "LowZ  %8.6f,%8.6f,%8.6f  %8.6f,%8.6f,%8.6f   %8.6f,%8.6f,%8.6f ", DYTag0No,DYTag0JECUp,DYTag0JECDown, DYTag1No,DYTag1JECUp,DYTag1JECDown, DYTag2No,DYTag2JECUp,DYTag2JECDown         ) ; 
       fprintf (outfulltable, "                                                 \n") ; 
       fprintf (outfulltable, "TF  %8.6f,%8.6f,%8.6f,%8.6f,%8.6f  %8.6f,%8.6f,%8.6f,%8.6f,%8.6f   %8.6f,%8.6f,%8.6f,%8.6f,%8.6f       ", TF0No,TF0UU,TF0DD,TF0UD,TF0DU,                      TF1No,TF1UU,TF1DD,TF1UD,TF1DU,  TF2No,TF2UU,TF2DD,TF2UD,TF2DU     ) ; 
       fprintf (outfulltable, "                                                 \n") ; 

    
  }
      fclose (outfulltable);
}  
}
