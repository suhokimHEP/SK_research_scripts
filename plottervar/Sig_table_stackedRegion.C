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

void print_hist(TH1F* h, TString name, FILE* file){

  fprintf(file, "%s", name.Data());
  for(int i=1; i<=2; i++){
    TString toprint = ", ";
    if(i==2){toprint += h->Integral(2,-1);}
    else{toprint += h->GetBinContent(i);}
    fprintf(file, "%s", toprint.Data());
  }
  fprintf(file,"\n");


}

void Sig_table_stackedRegion(TString region, Bool_t dolog, Bool_t HIP, Bool_t doctau, Bool_t useEOS, TString description)
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

 //inpath = inpath+aversion+"/";
 inpath = outpath+aversion+"/"+region+"/";
 outpath = outpath+aversion+"/"+region+"/";

 TString extraname = "";

 // lumi scaling by era
 Float_t MCSF = 1.;
 Float_t lumifb = 58670. ;
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
 std::vector<TString> uncbins;
 uncbins.clear();
 uncbins.push_back("_ESFUp"       );    
//// uncbins.push_back("_JECDown"     );    

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

 // initialize histogram files
 TFile* file_ZH_NoUnc                                ;
 TFile* file_ZH_JECUp                                ;
 TFile* file_ZH_JECDown                                ;
 TFile* file_ggZH_NoUnc                                ;
 TFile* file_ggZH_JECUp                                ;
 TFile* file_ggZH_JECDown                                ;

 // initialize histos
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
     TString logname = outpath+"tables/"+uncbin+"_full_text"; 
      outfulltable = fopen (logname+".txt","w");
       //fprintf (outfulltable, "Signal Point, 0-Tag central/up/down, 1-Tag central/up/down, 2-Tag central/up/down:\\\\\n") ; 
       if(region.Contains("DY")){fprintf (outfulltable, "Signal Point, LowZ 0-Tag up/down 1-Tag up/down 2-Tag up/down") ; 
       fprintf (outfulltable, "                                                 \n") ;} 
       else{fprintf (outfulltable, "HighZ 0-Tag up/down 1-Tag up/down 2-Tag up/down") ; 
       fprintf (outfulltable, "                                                 \n") ;} 
for(unsigned int k=0; k<MSbins.size(); ++k){
 //file_Sig                    = TFile::Open( inpath + "Sig_MS-55_ctauS-100_"+region+".root"                 ) ;
 TString MSsample = MSbins[k];
 string mssample = MSbins[k];
 // load histogram files
 //file_DY10to50                = TFile::Open( inpath + "DYJetsToLL_M-10to50_"+region+"_histograms.root"             ) ; 
cout<<"where"<<endl;

 // Start looping over variables, systematic uncertainty bins, make plots / tables / root files
  for(unsigned int j=0; j<variables.size(); ++j){
   TString variable = variables[j];

   for(unsigned int tt=0; tt<loopEnd; ++tt){
    TString uncbin = uncbins[tt];
    //Override drawData for nTag signal region
 file_ZH_NoUnc                    = TFile::Open( inpath +region+"_"+variable+"_log"+uncbin+"_"+MSsample+".root"                 ) ;
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
     //h_DY10to50                        = (TH1F*)file_DY10to50                         ->Get("h_"+varname+uncbin)->Clone( "DY10to50"                        +uncbin ) ;
     h_ZH_NoUnc       = (TH1F*)file_ZH_NoUnc    ->Get("Sig_NoUnc" )->Clone( "ZH_NoUnc" ) ;
     h_ZH_JECUp       = (TH1F*)file_ZH_NoUnc    ->Get("Sig_UncUp" )->Clone( "ZH_JECUp" ) ;
     h_ZH_JECDown       = (TH1F*)file_ZH_NoUnc    ->Get("Sig_UncDown" )->Clone( "ZH_JECDown" ) ;

	cout<<"here"<<endl;
     // h_DY->Add(h_DY10to50           ); 

     h_ZH_NoUnc   = (TH1F*) h_ZH_NoUnc    ->Clone( "ZH_NoUnc " ) ;
     h_ZH_JECUp   = (TH1F*) h_ZH_JECUp    ->Clone( "ZH_JECUp " ) ;
     h_ZH_JECDown   = (TH1F*) h_ZH_JECDown    ->Clone( "ZH_JECDown " ) ;
     // rescale MC to match eras used
     //h_ZH_NoUnc  ->Scale(MCSF);
     //h_ZH_JECUp  ->Scale(MCSF);
     //h_ZH_JECDown  ->Scale(MCSF);

     h_Sig_NoUnc  = (TH1F*) h_ZH_NoUnc   ->Clone( "Sig_NoUnc" ) ;
     h_Sig_JECUp   = (TH1F*) h_ZH_JECUp    ->Clone( "Sig_JECUp" ) ;
     h_Sig_JECDown    = (TH1F*) h_ZH_JECDown     ->Clone( "Sig_JECDown" ) ;
     h_bkgtotal= (TH1F*)h_Sig_NoUnc->Clone("bkgtotal");
    Float_t Sig_NoUnc_tag0 = h_Sig_NoUnc->GetBinContent(1);
    Float_t Sig_JECUp_tag0 = h_Sig_JECUp->GetBinContent(1);
    Float_t Sig_JECDown_tag0 = h_Sig_JECDown->GetBinContent(1);
    Float_t Sig_NoUnc_tag1 = h_Sig_NoUnc->GetBinContent(2);
    Float_t Sig_JECUp_tag1 = h_Sig_JECUp->GetBinContent(2);
    Float_t Sig_JECDown_tag1 = h_Sig_JECDown->GetBinContent(2);
    Float_t Sig_NoUnc_tag2 = h_Sig_NoUnc->GetBinContent(3);
    Float_t Sig_JECUp_tag2 = h_Sig_JECUp->GetBinContent(3);
    Float_t Sig_JECDown_tag2 = h_Sig_JECDown->GetBinContent(3);



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
       sigleg->SetBorderSize(0);
       sigleg->SetFillColor(kWhite);
	string legendprint = mssample;
	legendprint += uncbin;
	strcpy(charlegendprint,legendprint.c_str());	
       //sigleg->AddEntry(h_Sig_MS55ct100   , "no", "l" ) ;
       sigleg->AddEntry(h_Sig_JECUp   , "Sig_JECUp", "l" ) ;
       sigleg->AddEntry(h_Sig_NoUnc   , "Sig_NoUnc  ", "l" ) ;
	if(uncbin=="_JECUp") sigleg->AddEntry(h_Sig_JECDown   , "Sig JECDown", "l" ) ;
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

       h_Sig_JECUp->SetLineColor(kRed);
       h_Sig_JECUp->SetLineWidth(4);
       h_Sig_JECUp->SetLineStyle(2);
       h_Sig_JECUp->Draw("hist") ;
       h_Sig_JECUp->SetMaximum(5000) ;
       h_Sig_JECUp->SetMinimum(.01) ;
       h_Sig_NoUnc->SetLineColor(kBlack);
       h_Sig_NoUnc->SetLineWidth(4);
       h_Sig_NoUnc->Draw("hist sames") ;
	if(uncbin == "_JECUp"){
       h_Sig_JECDown->SetLineColor(kBlue);
       h_Sig_JECDown->SetLineWidth(4);
       h_Sig_JECDown->SetLineStyle(2);
       h_Sig_JECDown->Draw("hist sames") ;
	}
       sigleg->Draw();
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
	if(uncbin == "_JECUp"){
        h_ratio2 = (TH1F*)h_Sig_JECDown->Clone("ratio");
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
       h_ratio->GetYaxis()->SetRangeUser(0.0,2.0);
	if(uncbin == "_AMaxUp"|| uncbin == "_IPSigUp" || uncbin == "_TAUp" || uncbin == "_TagVarsUp"){h_ratio->GetYaxis()->SetRangeUser(0.0,2.0);}
       h_ratio->Draw("HIST p");  // draw first to get ranges set internally inside root
       //h_ratio2->SetMarkerStyle(20);
       //h_ratio2->SetMarkerColor(kBlue);
       //h_ratio2->SetMarkerSize(1);
              
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
       //h_ratio2->Draw("HIST p same");  // draw first to get ranges set internally inside root
     }
     else{
      // ratiopad->Clear();
     }

     // save canvas
     //canvas->SaveAs(outname+description+"_"+MSsample+".png");
     //canvas->SaveAs(outname+description+"_"+MSsample+".pdf");
  
// save histograms into single root file
       //fprintf (outfulltable, "%s, %8.6f/%8.6f/%8.6f, %8.6f/%8.6f/%8.6f, %8.6f/%8.6f/%8.6f\\\\\n",mssample.c_str(), Sig_NoUnc_tag0,Sig_JECUp_tag0,Sig_JECDown_tag0, Sig_NoUnc_tag1,Sig_JECUp_tag1,Sig_JECDown_tag1, Sig_NoUnc_tag2,Sig_JECUp_tag2,Sig_JECDown_tag2 ) ; 
       //fprintf (outfulltable, "%s, %8.6f/%8.6f/%8.6f, %8.6f/%8.6f/%8.6f, %8.6f/%8.6f/%8.6f\\\\\n",mssample.c_str(), Sig_NoUnc_tag0/Sig_NoUnc_tag0,Sig_JECUp_tag0/Sig_NoUnc_tag0,Sig_JECDown_tag0/Sig_NoUnc_tag0, Sig_NoUnc_tag1/Sig_NoUnc_tag1,Sig_JECUp_tag1/Sig_NoUnc_tag1,Sig_JECDown_tag1/Sig_NoUnc_tag1, Sig_NoUnc_tag2/Sig_NoUnc_tag2,Sig_JECUp_tag2/Sig_NoUnc_tag2,Sig_JECDown_tag2/Sig_NoUnc_tag2 ) ; 
       //fprintf (outfulltable, "%s %8.6f/%8.6f %8.6f/%8.6f %8.6f/%8.6f\n",mssample.c_str(), Sig_JECUp_tag0,Sig_JECDown_tag0, Sig_JECUp_tag1,Sig_JECDown_tag1, Sig_JECUp_tag2,Sig_JECDown_tag2 ) ; 
       if(region.Contains("DY")){fprintf (outfulltable, "%s     %8.6f %8.6f     %8.6f %8.6f     %8.6f %8.6f\n",mssample.c_str(), Sig_JECUp_tag0/Sig_NoUnc_tag0,Sig_JECDown_tag0/Sig_NoUnc_tag0, Sig_JECUp_tag1/Sig_NoUnc_tag1,Sig_JECDown_tag1/Sig_NoUnc_tag1, Sig_JECUp_tag2/Sig_NoUnc_tag2,Sig_JECDown_tag2/Sig_NoUnc_tag2 );} 
       else{fprintf (outfulltable, "     %8.6f %8.6f     %8.6f %8.6f     %8.6f %8.6f\n", Sig_JECUp_tag0/Sig_NoUnc_tag0,Sig_JECDown_tag0/Sig_NoUnc_tag0, Sig_JECUp_tag1/Sig_NoUnc_tag1,Sig_JECDown_tag1/Sig_NoUnc_tag1, Sig_JECUp_tag2/Sig_NoUnc_tag2,Sig_JECDown_tag2/Sig_NoUnc_tag2 );} 

   } 
  }
}  
      fclose (outfulltable);
}
