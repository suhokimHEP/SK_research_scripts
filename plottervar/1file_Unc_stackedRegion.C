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

void DY_stackedRegion(TString region, Bool_t dolog, Bool_t HIP, Bool_t doctau, Bool_t useEOS, TString description)
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

 TString outpath = TString("../plots/");
 TString aversion = TString(getenv("aversion"));
 TString nversion = TString(getenv("nversion"));
 TString depot = TString(getenv("depot2"));
 TString inpath  = TString("../roots/");
 if(useEOS){
  inpath = "root://cmsxrootd.fnal.gov/"+depot+"/"+nversion+"/analyzed/"; 
}

 inpath = inpath+aversion+"/";
 outpath = outpath+aversion+"/"+region+"/";

 TString extraname = "";

 // lumi scaling by era
 Float_t MCSF = 1.;
 Float_t lumifb = 58670. ;
 MCSF = (lumifb)/20000.; 

 //TString extraname = "";
 if(dolog){
  extraname+="_log";
  outpath = outpath+"log/";
 }

 TString mdcommand = (TString)"mkdir -p "+outpath.Data();
 const int dir_err = system(mdcommand);
 TString mdcommandtable = (TString)"mkdir -p "+outpath.Data()+"tables/";
 const int dir_err2 = system(mdcommandtable);

 std::vector<string> MSbins;
 MSbins.push_back("DYJetsToLL_M-50"); 
 MSbins.push_back("TTJets"); 
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



 std::vector<TString> uncbins;
 uncbins.clear();
// uncbins.push_back("_EGSUp"       ); 
//// //uncbins.push_back("_EGSDown"     );    
// uncbins.push_back("_MESUp"       );    
//// //uncbins.push_back("_MESDown"     );    
// uncbins.push_back("_AMaxUp"      );    
////// uncbins.push_back("_AMaxDown"    );    
// uncbins.push_back("_IPSigUp"     );    
//////// uncbins.push_back("_IPSigDown"   );    
// uncbins.push_back("_TAUp"        );    
//////// uncbins.push_back("_TADown"      );    
// uncbins.push_back("_TagVarsUp"   ); 
//////// uncbins.push_back("_TagVarsDown" );  
 uncbins.push_back("_MSFUp"       );    
//// uncbins.push_back("_MSFDown"     );    

 int loopEnd;
 if (doUncPlots) loopEnd=uncbins.size(); else loopEnd=1;
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

 float pad_bottom = 0;
 if(drawData) pad_bottom = 0.25;
 TPad *plotpad  = new TPad("plotpad", "plotpad", 0, pad_bottom, 1, 1);
 plotpad->SetBottomMargin(0.12);
 if(drawData) plotpad->SetBottomMargin(0.04);
 plotpad->SetLeftMargin(lmarg);
 plotpad->SetRightMargin(rmarg);
 plotpad->SetFrameLineWidth(3);
 plotpad->SetLogy(dolog);
 plotpad->Draw();

 canvas->cd();
 TPad *ratiopad = new TPad("ratiopad", "ratiopad", 0, 0, 1, 0.25);
 ratiopad->SetTopMargin(0.04);
 ratiopad->SetBottomMargin(0.4);
 ratiopad->SetFrameLineWidth(3);
 ratiopad->SetLeftMargin(lmarg);
 ratiopad->SetRightMargin(rmarg);
 ratiopad->SetLogy(0);
 ratiopad->SetGrid();
 if(drawData) ratiopad->Draw();
 canvas->cd();

 TText* title = new TText(1,1,"") ;
 title->SetTextSize(0.06);
 title->SetTextColor(kBlack);
 title->SetTextAlign(11);
 title->SetTextFont(62);
 
 TText* extra = new TText(1,1,"") ;
 extra->SetTextSize(0.05);
 extra->SetTextColor(kBlack);
 extra->SetTextAlign(11);
 //extra->SetTextAlign(13);
 extra->SetTextFont(52);
 
 TText* extra2 = new TText(1,1,"") ;
 extra2->SetTextSize(0.03);
 extra2->SetTextColor(kBlack);
 extra2->SetTextAlign(11);
 //extra2->SetTextAlign(13);
 extra2->SetTextFont(62);
 
 TText* lumi = new TText(1,1,"") ;
 lumi->SetTextSize(0.05);
 lumi->SetTextColor(kBlack);
 lumi->SetTextAlign(31);
 lumi->SetTextFont(42);

 TFile* file_DY50                                ;
 // initialize histos
 TH1F* h_ZH_JECUp                                ;
 TH1F* h_ZH_NoUnc      ;

 TH1F* h_ZH_JECUp_MESDown      ;
 TH1F* h_ZH_JECUp_EGSDown      ;
 TH1F* h_ZH_JECDown      ;
 TH1F* h_ZH_JECUp_AMaxDown      ;
 TH1F* h_ZH_JECUp_IPSigDown      ;
 TH1F* h_ZH_JECUp_TADown      ;
 TH1F* h_ZH_JECUp_TagVarsDown      ;

 TH1F* h_ratio ;
 TH1F* h_ratio2 ;
 TH1F* h_ratiostaterr ;
 TH1F* h_bkgtotal ;


 // (combined) histos to be made
 TH1F* h_Sig_JECUp     ;
 TH1F* h_Sig_NoUnc  ;
 TH1F* h_Sig_JECUp_MESDown  ;
 TH1F* h_Sig_JECUp_EGSDown  ;
 TH1F* h_Sig_JECDown  ;
 TH1F* h_Sig_JECUp_AMaxDown      ;
 TH1F* h_Sig_JECUp_IPSigDown      ;
 TH1F* h_Sig_JECUp_TADown      ;
 TH1F* h_Sig_JECUp_TagVarsDown      ;

 TH1F* h_Data   ;
for(unsigned int k=0; k<MSbins.size(); ++k){
 TString MSsample = MSbins[k];
 string mssample = MSbins[k];
 file_DY50                    = TFile::Open( inpath +  MSsample+"_"+region+"_histograms.root"                 ) ;
 // Start looping over variables, systematic uncertainty bins, make plots / tables / root files

 // Start looping over variables, systematic uncertainty bins, make plots / tables / root files
  for(unsigned int j=0; j<variables.size(); ++j){
   TString variable = variables[j];

   for(unsigned int tt=0; tt<loopEnd; ++tt){
    TString uncbin = uncbins[tt];
    //Override drawData for nTag signal region
    if(region.Contains("ZH") && 
       (variable=="nSelectedAODCaloJetTag" || 
	variable.Contains("Log10IPSig") || 
	variable.Contains("Log10TrackAngle") || 
	variable.Contains("AlphaMax")) ) {
      drawData=true;
    }
    if(variable.Contains("Raw")){
     drawData=true;
    }
    if( variable.Contains("NMinus")   ||
	variable.Contains("Onecut")   ||               
	variable.Contains("Cutflow") ) {
     dolog=true;
    }

    Bool_t domaketable = kTRUE;
    if(j==0){
     domaketable = kTRUE;
    }
     TString varname = region+"_"+variable;

     printf("plotting  h_%s \n",varname.Data());

     TString outname = outpath+varname+extraname+uncbin; 
     TString fulllogname = outpath+"tables/full_"+varname+extraname+uncbin; 
     TString smalllogname = outpath+"tables/small_"+varname+extraname+uncbin; 
     TString tinylogname = outpath+"tables/tiny_"+varname+extraname+uncbin; 
     //cout << "logname: " << logname << endl;
     // get histograms from files
     //h_Sig_JECUp10to50                        = (TH1F*)file_DY10to50                         ->Get("h_"+varname+uncbin)->Clone( "DY10to50"                        +uncbin ) ;
     h_ZH_JECUp                            = (TH1F*)file_DY50                             ->Get("h_"+varname+uncbin)->Clone( "ZH_UncUp"                            +uncbin ) ;
     h_ZH_NoUnc       = (TH1F*)file_DY50    ->Get("h_"+varname )->Clone( "ZH_NoUnc" ) ;
     //h_ZH_JECUp_MESDown       = (TH1F*)file_DY50    ->Get("h_"+varname+"_MESDown" )->Clone( "DY50_MESDown" ) ;
     //h_ZH_JECUp_EGSDown       = (TH1F*)file_DY50    ->Get("h_"+varname+"_EGSDown" )->Clone( "DY50_EGSDown" ) ;
     h_ZH_JECDown       = (TH1F*)file_DY50    ->Get("h_"+varname+"_MSFDown" )->Clone( "ZH_UncDown" ) ;
     //h_ZH_JECUp_AMaxDown       = (TH1F*)file_DY50    ->Get("h_"+varname+"_AMaxDown" )->Clone( "DY50_AMaxDown" ) ;
     //h_ZH_JECUp_IPSigDown       = (TH1F*)file_DY50    ->Get("h_"+varname+"_IPSigDown" )->Clone( "DY50_IPSigDown" ) ;
     //h_ZH_JECUp_TADown       = (TH1F*)file_DY50    ->Get("h_"+varname+"_TADown" )->Clone( "DY50_TADown" ) ;
     //h_ZH_JECUp_TagVarsDown       = (TH1F*)file_DY50    ->Get("h_"+varname+"_TagVarsDown" )->Clone( "DY50_TagVarsDown" ) ;

	cout<<"here"<<endl;
     h_Sig_JECUp = (TH1F*)h_ZH_JECUp->Clone("Sig_UncUp");
     // h_Sig_JECUp->Add(h_Sig_JECUp10to50           ); 

     h_Sig_NoUnc   = (TH1F*) h_ZH_NoUnc    ->Clone( "Sig_NoUnc " ) ;
     //h_Sig_JECUp_MESDown   = (TH1F*) h_ZH_JECUp_MESDown    ->Clone( "DY_MESDown " ) ;
     //h_Sig_JECUp_EGSDown   = (TH1F*) h_ZH_JECUp_EGSDown    ->Clone( "DY_EGSDown " ) ;
     h_Sig_JECDown   = (TH1F*) h_ZH_JECDown    ->Clone( "Sig_UncDown " ) ;
     //h_Sig_JECUp_AMaxDown   = (TH1F*) h_ZH_JECUp_AMaxDown    ->Clone( "DY_AMaxDown " ) ;
     //h_Sig_JECUp_IPSigDown   = (TH1F*) h_ZH_JECUp_IPSigDown    ->Clone( "DY_IPSigDown " ) ;
     //h_Sig_JECUp_TADown   = (TH1F*) h_ZH_JECUp_TADown    ->Clone( "DY_TADown " ) ;
     //h_Sig_JECUp_TagVarsDown   = (TH1F*) h_ZH_JECUp_TagVarsDown    ->Clone( "DY_TagVarsDown " ) ;
     // rescale MC to match eras used
     h_Sig_JECUp         ->Scale(MCSF); 
     //h_Sig_JECUp         ->Scale(1.038*MCSF); 
     h_Sig_NoUnc  ->Scale(MCSF);
     //h_Sig_JECUp_MESDown  ->Scale(MCSF);
     //h_Sig_JECUp_EGSDown  ->Scale(MCSF);
     h_Sig_JECDown  ->Scale(MCSF);
     //h_Sig_JECDown  ->Scale(1.005*MCSF);
     //h_Sig_JECUp_AMaxDown  ->Scale(MCSF);
     //h_Sig_JECUp_IPSigDown  ->Scale(MCSF);
     //h_Sig_JECUp_TADown  ->Scale(MCSF);
     //h_Sig_JECUp_TagVarsDown  ->Scale(MCSF);

     h_bkgtotal= (TH1F*)h_Sig_JECUp->Clone("bkgtotal");

     // Integrals
     //Float_t  int_DY10to50                 = h_Sig_JECUp10to50                        ->Integral(0,-1); 
     Float_t  int_DY50                     = h_ZH_JECUp                            ->Integral(0,-1); 

// integrals of summed histograms
     Float_t int_DY        = h_Sig_JECUp       ->Integral(0,-1); 
     // set attributes
     h_Sig_JECUp         -> SetLineColor(kBlack); 
     h_Sig_JECUp        ->SetFillStyle(1001);
     h_Sig_JECUp        ->SetLineColor(kBlack); 
     h_Sig_JECUp        ->SetLineWidth(0);
     h_bkgtotal->SetFillColorAlpha(kYellow+1, 0.7);
     h_bkgtotal->SetFillStyle(1001);

     std::vector<TH1F *> v;
     if(useAlt){
       v.push_back(h_Sig_JECUp);
     }
     else {
       v.push_back(h_Sig_JECUp);
     }
     
     // make stack
     THStack *bgstack = new THStack("bgstack","");
     if(dolog){
      std::sort(v.begin(), v.end(),
		[](TH1F *a, TH1F *b) { return a->Integral() < b->Integral(); });
      for(int zz=0; zz<v.size(); zz++)
      {
       bgstack->Add(v[zz]);
       //cout <<v[zz]->Integral()<<std::endl;
      }
     }
     else{
       if(useAlt){
	 bgstack->Add(h_Sig_JECUp      ); 
       }
       else {
	 bgstack->Add(h_Sig_JECUp         ); 
       }

     }
      double tot = 0.0; 
     // make legend
	char charlegendprint[80];
     TLegend *sigleg = new TLegend(0.54,0.6,0.88,0.8);
     if(drawSignal){
       sigleg->SetBorderSize(0);
       sigleg->SetFillColor(kWhite);
	string legendprint = mssample;
	legendprint += uncbin;
	strcpy(charlegendprint,legendprint.c_str());	
       //sigleg->AddEntry(h_Sig_MS55ct100   , "no", "l" ) ;
       sigleg->AddEntry(h_Sig_JECUp   , charlegendprint, "l" ) ;
       sigleg->AddEntry(h_Sig_NoUnc   , " NoUnc  ", "l" ) ;
	//if(uncbin=="_MESUp") sigleg->AddEntry(h_Sig_JECUp_MESDown   , "DY50 MESDown", "l" ) ;
	//if(uncbin=="_EGSUp") sigleg->AddEntry(h_Sig_JECUp_EGSDown   , "DY50 EGSDown", "l" ) ;
	if(uncbin=="_MSFUp") sigleg->AddEntry(h_Sig_JECDown   , " MSFDown", "l" ) ;
	//if(uncbin=="_AMaxUp") sigleg->AddEntry(h_Sig_JECUp_AMaxDown   , "DY50 AMaxDown", "l" ) ;
	//if(uncbin=="_IPSigUp") sigleg->AddEntry(h_Sig_JECUp_IPSigDown   , "DY50 IPSigDown", "l" ) ;
	//if(uncbin=="_TAUp") sigleg->AddEntry(h_Sig_JECUp_TADown   , "DY50 TADown", "l" ) ;
	//if(uncbin=="_TagVarsUp") sigleg->AddEntry(h_Sig_JECUp_TagVarsDown   , "DY50 TagVarsDown", "l" ) ;
     }

     // set max and draw
     double_t ymax;
     ymax = std::max(h_Sig_JECUp->GetMaximum(), h_bkgtotal->GetMaximum() );
     if(dolog){
      //bgstack->SetMaximum(50000*ymax); 
      //bgstack->SetMinimum(1.0e-6);
      bgstack->SetMaximum(1000000); 
      bgstack->SetMinimum(1.0e-1);
     } 
     else {
      bgstack->SetMaximum(ymax*2);
     }
      
     plotpad->cd();
     bgstack->Draw("hist");
     //bgstack->Draw("hist e");
     bgstack->GetYaxis()->SetTitle("Events");
     //bgstack->GetYaxis()->SetTitleOffset(1.85);
     bgstack->GetYaxis()->SetTitleSize(40);
     bgstack->GetYaxis()->SetTitleFont(43);
     bgstack->GetYaxis()->SetTitleOffset(1.75);
     bgstack->GetXaxis()->SetTitle(region+"_"+varname + "    "+description);
     if(!drawData){
       bgstack->GetXaxis()->SetTitleSize(40);
       bgstack->GetXaxis()->SetTitleFont(43);
       bgstack->GetXaxis()->SetTitle(varname + "    "+description);
       //bgstack->GetXaxis()->SetTitle((TString)h_Data->GetTitle()+description);
       bgstack->GetXaxis()->SetTitleOffset(1);
       bgstack->GetXaxis()->SetLabelFont(43); //43 Absolute font size in pixel (precision 3)
       bgstack->GetXaxis()->SetLabelSize(40);//20
       bgstack->GetYaxis()->SetTitleOffset(1);
     }
     
     //h_bkgtotal->Draw("e2 sames");
     if(drawData){
       //h_Data->Draw("sames E"); 
     }

     if(drawSignal){

       h_Sig_JECUp->SetLineColor(kRed);
       h_Sig_JECUp->SetLineWidth(4);
       h_Sig_JECUp->SetLineStyle(2);
       h_Sig_JECUp->Draw("hist") ;
       h_Sig_JECUp->SetMaximum(10000000) ;
       h_Sig_JECUp->SetMinimum(.1) ;
       h_Sig_NoUnc->SetLineColor(kBlack);
       h_Sig_NoUnc->SetLineWidth(4);
       h_Sig_NoUnc->Draw("hist sames") ;
	if(uncbin == "_MESUp"){
       h_Sig_JECUp_MESDown->SetLineColor(kBlue);
       h_Sig_JECUp_MESDown->SetLineWidth(4);
       h_Sig_JECUp_MESDown->SetLineStyle(2);
       h_Sig_JECUp_MESDown->Draw("hist sames") ;
	}
	
	if(uncbin == "_EGSUp"){
       h_Sig_JECUp_EGSDown->SetLineColor(kBlue);
       h_Sig_JECUp_EGSDown->SetLineWidth(4);
       h_Sig_JECUp_EGSDown->SetLineStyle(2);
       h_Sig_JECUp_EGSDown->Draw("hist sames") ;
	}
	
	if(uncbin == "_MSFUp"){
       h_Sig_JECDown->SetLineColor(kBlue);
       h_Sig_JECDown->SetLineWidth(4);
       h_Sig_JECDown->SetLineStyle(2);
       h_Sig_JECDown->Draw("hist sames") ;
	}
	if(uncbin == "_AMaxUp"){
       h_Sig_JECUp_AMaxDown->SetLineColor(kBlue);
       h_Sig_JECUp_AMaxDown->SetLineWidth(4);
       h_Sig_JECUp_AMaxDown->SetLineStyle(2);
       h_Sig_JECUp_AMaxDown->Draw("hist sames") ;
	}
	if(uncbin == "_IPSigUp"){
       h_Sig_JECUp_IPSigDown->SetLineColor(kBlue);
       h_Sig_JECUp_IPSigDown->SetLineWidth(4);
       h_Sig_JECUp_IPSigDown->SetLineStyle(2);
       h_Sig_JECUp_IPSigDown->Draw("hist sames") ;
	}
	if(uncbin == "_TAUp"){
       h_Sig_JECUp_TADown->SetLineColor(kBlue);
       h_Sig_JECUp_TADown->SetLineWidth(4);
       h_Sig_JECUp_TADown->SetLineStyle(2);
       h_Sig_JECUp_TADown->Draw("hist sames") ;
	}
	if(uncbin == "_TagVarsUp"){
       h_Sig_JECUp_TagVarsDown->SetLineColor(kBlue);
       h_Sig_JECUp_TagVarsDown->SetLineWidth(4);
       h_Sig_JECUp_TagVarsDown->SetLineStyle(2);
       h_Sig_JECUp_TagVarsDown->Draw("hist sames") ;
	}
       sigleg->Draw();
 }
     char lumistring [50];
     int dummy; 

     // add titles
     title->DrawTextNDC(0.2,0.91,"CMS");
     extra->DrawTextNDC(0.3,0.91,"Preliminary");
      extra2->DrawTextNDC(0.51,0.91,"2018");
      dummy=sprintf (lumistring, "%0.1f", lumifb/1000.);
     //lumi->DrawTextNDC(0.9,0.91,"35.9 /fb (13 TeV)");
     lumi->DrawTextNDC(0.9,0.91,(TString)lumistring+" /fb (13 TeV)");
     
     if(drawData){
       ratiopad->cd();
       h_ratio = (TH1F*)h_Sig_JECUp->Clone("ratio");
       if(h_Sig_JECUp->Integral(-1,-1)>0){
	 h_ratio->Divide(h_Sig_NoUnc);
       }
	if(uncbin == "_MESUp"){
        h_ratio2 = (TH1F*)h_Sig_JECUp_MESDown->Clone("ratio");
	h_ratio2->Divide(h_Sig_NoUnc);
	}
	if(uncbin == "_EGSUp"){
        h_ratio2 = (TH1F*)h_Sig_JECUp_EGSDown->Clone("ratio");
  	h_ratio2->Divide(h_Sig_NoUnc);
	}
	if(uncbin == "_MSFUp"){
        h_ratio2 = (TH1F*)h_Sig_JECDown->Clone("ratio");
	h_ratio2->Divide(h_Sig_NoUnc);
	}
	if(uncbin == "_AMaxUp"){
        h_ratio2 = (TH1F*)h_Sig_JECUp_AMaxDown->Clone("ratio");
	h_ratio2->Divide(h_Sig_NoUnc);
	}
	if(uncbin == "_IPSigUp"){
        h_ratio2 = (TH1F*)h_Sig_JECUp_IPSigDown->Clone("ratio");
	h_ratio2->Divide(h_Sig_NoUnc);
	}
	if(uncbin == "_TAUp"){
        h_ratio2 = (TH1F*)h_Sig_JECUp_TADown->Clone("ratio");
	h_ratio2->Divide(h_Sig_NoUnc);
	}
	if(uncbin == "_TagVarsUp"){
        h_ratio2 = (TH1F*)h_Sig_JECUp_TagVarsDown->Clone("ratio");
	h_ratio2->Divide(h_Sig_NoUnc);
	}
       h_ratio->SetTitle(" ");
       // Y axis ratio plot settings
       h_ratio->GetYaxis()->SetTitleSize(30);
       h_ratio->GetYaxis()->SetTitleFont(43);
       h_ratio->GetYaxis()->SetTitleOffset(1.55);
       h_ratio->GetYaxis()->SetLabelFont(43); // Absolute font size in pixel (precision 3)
       h_ratio->GetYaxis()->SetLabelSize(20);
       h_ratio->GetYaxis()->SetNdivisions(-105);
       h_ratio->GetYaxis()->SetTitle(uncbin+"/NoUnc");
       // X axis ratio plot settings
       h_ratio->GetXaxis()->SetTitleSize(40);
       h_ratio->GetXaxis()->SetTitleFont(43);
       //h_ratio->GetXaxis()->SetTitle((TString)h_Data->GetTitle()+description);
       //h_ratio->GetXaxis()->SetTitle(region+"_"+(TString)h_Data->GetTitle()+description);
       h_ratio->GetXaxis()->SetTitleOffset(4.0);
       h_ratio->GetXaxis()->SetLabelFont(43); //43 Absolute font size in pixel (precision 3)
       h_ratio->GetXaxis()->SetLabelSize(30);//20
       h_ratio->SetMarkerStyle(20);
       h_ratio->SetMarkerColor(kRed);
       h_ratio->SetMarkerSize(1);
       h_ratio->GetYaxis()->SetRangeUser(0.8,1.2);
	if(uncbin == "_AMaxUp"|| uncbin == "_IPSigUp" || uncbin == "_TAUp" || uncbin == "_TagVarsUp"){h_ratio->GetYaxis()->SetRangeUser(0.0,2.0);}
       h_ratio->Draw("HIST p");  // draw first to get ranges set internally inside root
       h_ratio2->SetMarkerStyle(20);
       h_ratio2->SetMarkerColor(kBlue);
       h_ratio2->SetMarkerSize(1);
              
       h_ratiostaterr = (TH1F*)h_bkgtotal->Clone("ratiostaterr");
       h_ratiostaterr->Divide(h_bkgtotal);
       
       ratiopad->Update();       // need to update pad to get X min/max
       TLine *line = new TLine(ratiopad->GetUxmin(),1,ratiopad->GetUxmax(),1);
       line->SetLineColor(kBlue);
       line->SetLineWidth(3);
       line->SetLineStyle(9);
       //h_ratiostaterr->Draw("e2 same");

       line->Draw();
       h_ratio->Draw("HIST p same"); // draw points above line
       h_ratio2->Draw("HIST p same");  // draw first to get ranges set internally inside root
     }
     else{
      // ratiopad->Clear();
     }
	cout<<"Sample Name:"<<mssample<<endl; 
	cout<<"0Tag bin MSFUp/NoUnc:"<<h_Sig_JECUp->GetBinContent(1)/h_Sig_NoUnc->GetBinContent(1)<<endl;
 	cout<<"1Tag bin MSFUp/NoUnc:"<<h_Sig_JECUp->GetBinContent(2)/h_Sig_NoUnc->GetBinContent(2)<<endl;
 	cout<<"2Tag bin MSFUp/NoUnc:"<<h_Sig_JECUp->GetBinContent(3)/h_Sig_NoUnc->GetBinContent(3)<<endl;
 	cout<<"0Tag bin MSFDown/NoUnc:"<<h_Sig_JECDown->GetBinContent(1)/h_Sig_NoUnc->GetBinContent(1)<<endl;
 	cout<<"1Tag bin MSFDown/NoUnc:"<<h_Sig_JECDown->GetBinContent(2)/h_Sig_NoUnc->GetBinContent(2)<<endl;
 	cout<<"2Tag bin MSFDown/NoUnc:"<<h_Sig_JECDown->GetBinContent(3)/h_Sig_NoUnc->GetBinContent(3)<<endl;

     // save canvas
     canvas->SaveAs(outname+description+"_"+MSsample+".png");
     canvas->SaveAs(outname+description+"_"+MSsample+".pdf");
 	cout<<"--------------------------------"<<endl; 
// save histograms into single root file
     TFile *outfile = TFile::Open(outname+description+"_"+MSsample+".root","RECREATE");
     h_Sig_JECUp          ->Write();
     h_Sig_NoUnc          ->Write();
     h_Sig_JECDown          ->Write();
     h_bkgtotal    ->Write();
   
  if( drawData ){
      h_ratio       ->Write();
      //h_ratiostaterr->Write();
     }
     bgstack       ->Write();
   } 
  }
}  
}
