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
#include <math.h>

void P2draw(int Radius){
std::vector<int> Radii;
Radii.push_back(Radius);
std::vector<string> Regions;
//Regions.push_back("TwoMuDY");
for(int i =9; i < 23; i++){
string mindex = std::to_string(i);
Regions.push_back(mindex);
}
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
 c1->Clear();
 c1->cd();
c1->SetGrid();
gPad->SetLeftMargin(0.13);
gPad->SetBottomMargin(0.12);
gPad->SetTickx();
gPad->SetTicky();
//gPad->SetLogy();
gStyle->SetOptStat(0);
gStyle->SetLineWidth(3);
gStyle->SetHistLineWidth(3);
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
_file0 = TFile::Open("root://cmsxrootd.fnal.gov//store/group/lpchbb/LLDJntuples/Phase2/RelValTTbar_14TeV/crab_TTBar3/210224_202440/0000/hadd.root");
TTree* mytree16 = (TTree*)_file0->Get("Phase2/EventTree");


for(int j = 0; j < Radii.size(); j++){
for(int i = 0; i < Regions.size(); i++){
//char radius[20];    
//char uradius[20];    
//sprintf(radius, "%d", Radii.at(i));
//sprintf(uradius, "%d", Radii.at(i)+2);
int newint = Radii.at(j)+1;



string rad= std::to_string(Radii.at(j));
string urad= std::to_string(newint);
string layer = Regions.at(i);
TString Layer = layer;
TString Rad = rad;
const char *cstr = layer.c_str();
const char *radius = rad.c_str();
const char *uradius = urad.c_str();
TH1F* hVar2 = new TH1F(Layer,Layer,80, -4, 0);
TCut cut1 = Form("SimhitLayer==%s",cstr);
TCut cut2 = Form("SimhitGPr>%s",radius);
TCut cut3 = Form("SimhitGPr<%s",uradius);
TH1F* hVar = new TH1F();
mytree16->Draw("SimhitLogEnergy>>SimhitEn(80,-4,0)",cut1&&cut2&&cut3);
hVar = (TH1F*)mytree16->GetHistogram();
//hVar->SetTitle("Layer-"+Layer+"_RingNum-"+NRad+" Simhit Energy");
hVar->SetTitle("Layer-"+Layer+"_RingRadius-"+Rad+"cm Simhit Energy");
hVar->GetXaxis()->SetTitle("Log10(Energy)(GeV)");
float outlier = hVar->Integral(57,-1);
float tot = hVar->Integral(0,-1);
float ratio = outlier/tot;
TString soutlier = "#geq 70MeV(100MIPs):"+std::to_string(ratio);
//h0->GetXaxis()->SetTitle(Var);
//h0->GetYaxis()->SetTitle("Unit Integraled");
//h0->GetYaxis()->SetTitleOffset(1.3);
//
//h0->Scale(1./h0->Integral());
//h0->SetLineColor(3);
//legend =  new TLegend(0.55,0.65,0.75,0.75); 		
//legend->SetBorderSize(0);
//legend->SetNColumns(2);
//legend->SetFillColor(kWhite);
//legend->AddEntry(h0,"MC","l");
//legend->Draw();
TPaveText *fitbox = new TPaveText(.45,.8,.75,.9,"brNDC");
fitbox->SetBorderSize(1);
fitbox->SetFillColor(0);
fitbox->SetTextSize(0.023);
fitbox->AddText(soutlier);
fitbox->Draw();
title->DrawTextNDC(0.2,0.91,"CMS");
extra->DrawTextNDC(0.3,0.91,"Preliminary");
extra2->DrawLatexNDC(0.55,0.91,"Phase2 2026");

c1->Update();
c1->Modified();
c1->SaveAs("P2Simhit_L"+Layer+"_R"+Rad+".png");
//c1->Delete();
//k=raw_input('Press ENTER to exit');
}
}


}
