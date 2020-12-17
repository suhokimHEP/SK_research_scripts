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
#include <fstream>
#include <cstdlib> /* mkdir */

#include <stdlib.h>     /* getenv */

//void ratio161718(TString sample, TString inpath, TString outpath, TString nfiles, TString atfile){
void Cutflow(){
std::vector<TString> Regions;
//Regions.push_back("TwoMuDY");
Regions.push_back("TwoEleOffZ");

std::vector<TString> TV;
TV.push_back("RawCutflow");
std::vector<TString> Label = {"None","TwoEle","GoodVtx","ZWindow","pTOSSF>10GeV","OneJet","N/A","N/A"};
gROOT->ForceStyle(kTRUE);

TFile* _file0;
TFile* _file1;
TH1F* h0;
TH1F* h1;
TLegend *legend;
 TCanvas* c1 = new TCanvas("canvas","canvas",1100,900); 
gPad->SetLeftMargin(0.13);
gPad->SetBottomMargin(0.12);
gPad->SetTickx();
gPad->SetTicky();
gStyle->SetOptStat(0);
gStyle->SetLineWidth(3);
gStyle->SetHistLineWidth(3);
 c1->Clear();
 c1->cd();
c1->SetGrid();
// TPad *plotpad  = new TPad("plotpad", "plotpad", 0, 0, 1, 1);
// plotpad->SetBottomMargin(0.12);
// plotpad->SetBottomMargin(0.04);
// //plotpad->SetLeftMargin(lmarg);
// //plotpad->SetRightMargin(rmarg);
// plotpad->SetFrameLineWidth(3);
// //plotpad->SetLogy(dolog);
// plotpad->Draw();
//plotpad->cd();

//l = TLatex()
//l.SetTextAlign(13)
//l.SetTextSize(0.02)
//l.DrawLatexNDC(0.23,0.92,"CMS #it{Preliminary}           2017 DataSet B,2018 DataSet C  (13TeV)")
//l.DrawLatexNDC(0.23,0.62,"splitline{CMS #it{Preliminary}}{2016,2017,2018 full lumi}")
TText* title = new TText(1,1,"") ;
title->SetTextSize(0.045);
title->SetTextColor(kBlack);
title->SetTextAlign(11);
title->SetTextFont(62);

TText* extra = new TText(1,1,"") ;
extra->SetTextSize(0.03);
extra->SetTextColor(kBlack);
extra->SetTextAlign(11);
extra->SetTextFont(52);

TLatex* extra2 = new TLatex(1,1,"") ;
extra2->SetTextSize(0.025);
extra2->SetTextColor(kBlack);
extra2->SetTextAlign(11);
extra2->SetTextFont(62);


for(int i = 0; i < Regions.size(); i++)
	{for(int j = 0; j < TV.size(); j++)
	{
TString Channel = Regions.at(i);
TString Var = TV.at(j);
_file0 = TFile::Open("/uscms/home/skim2/nobackup/SK_research_scripts/temp/temproot/newTwoEleOffZ_DYJetsToLL_M-50_Vgamma.root");
_file1 = TFile::Open("/uscms/home/skim2/nobackup/SK_research_scripts/temp/temproot/newTwoEleOffZ_DYJetsToLL_M-50_Vgamma.root");
//_file0 = TFile::Open("/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/junk/DYJetsToLL_M-50_"+Channel+"_histograms.root");
//_file1 = TFile::Open("/uscms/home/skim2/nobackup/2018-LLDJ_slc7_700_CMSSW_10_2_5/src/2018lldj/analyzers/junk/Data_DoubleMuon_D_"+Channel+"_histograms.root");
//h0=(TH1F*)_file0->Get("h_%s_AllJets_AODCaloJet%s"%(Channel,Var))->Clone("h0");
//h1=(TH1F*)_file1->Get("h_%s_AllJets_AODCaloJet%s"%(Channel,Var))->Clone("h1");
h0=(TH1F*)_file0->Get("h_"+Channel+"_"+Var)->Clone("h0");
h1=(TH1F*)_file1->Get("h_"+Channel+"_"+Var)->Clone("h1");
//h0->SetTitle("Data&MC %s_%s Hist" %(Channel,Var));
//h0->GetXaxis()->SetTitle("%s" %Var);
h0->SetTitle("Data&MC "+Channel+"_"+Var+" Hist");
h0->GetXaxis()->SetTitle(Var);
h0->GetYaxis()->SetTitle("Unit Integraled");
h0->GetYaxis()->SetTitleOffset(1.3);

h0->Scale(1./h0->Integral());
h0->SetLineColor(3);
h1->Scale(1./h1->Integral());
h1->SetLineColor(4);
for (int k = 0; k<Label.size(); k++){
	h0->GetXaxis()->SetBinLabel(k+1,Label.at(k));
}
h0->Draw("hist");
h1->Draw("hist SAME");
legend =  new TLegend(0.55,0.65,0.75,0.75); 		
legend->SetBorderSize(0);
legend->SetNColumns(2);
legend->SetFillColor(kWhite);
legend->AddEntry(h0,"MC","l");
legend->AddEntry(h1,"Data","l");
legend->Draw();
title->DrawTextNDC(0.2,0.91,"CMS");
extra->DrawTextNDC(0.3,0.91,"Preliminary");
extra2->DrawLatexNDC(0.55,0.91,"Run2 2018       lumi 62.76/fb");

c1->Update();
c1->Modified();
c1->SaveAs("2018_"+Channel+"_"+Var+".png");
//c1->Delete();
//k=raw_input('Press ENTER to exit');
}}



}
