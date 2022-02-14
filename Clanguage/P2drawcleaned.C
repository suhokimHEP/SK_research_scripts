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

void P2eff(int Radius){
std::vector<int> Radii;
Radii.push_back(Radius);
std::vector<string> Regions;
//Regions.push_back("TwoMuDY");
for(int i =9; i < 23; i++){
string mindex = std::to_string(i);
Regions.push_back(mindex);
}
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
_file0 = TFile::Open("root://cmsxrootd.fnal.gov//store/group/lpchbb/LLDJntuples/Phase2_Rechit/RelValZMM_14/crab_ZMM_Full/210406_022806/0000/hadd.root");
TTree* mytree16 = (TTree*)_file0->Get("Phase2/EventTree");


for(int j = 0; j < Radii.size(); j++){
for(int i = 0; i < Regions.size(); i++){
int newint = Radii.at(j)+1;



string rad= std::to_string(Radii.at(j));
string urad= std::to_string(newint);
string layer = Regions.at(i);
TString Layer = layer;
TString Rad = rad;
const char *cstr = layer.c_str();
const char *radius = rad.c_str();
const char *uradius = urad.c_str();
TCut cut1 = Form("SimhitLayer==%s",cstr);
TCut cut2 = Form("SimhitGPr>%s",radius);
TCut cut3 = Form("SimhitGPr<%s",uradius);
TH1F* hVar = new TH1F();
mytree16->Draw("SimhitLogEnergy>>SimhitEn(80,-4,0)",cut1&&cut2&&cut3);
hVar = (TH1F*)mytree16->GetHistogram();
hVar->SetTitle("Layer-"+Layer+"_RingRadius-"+Rad+"cm Simhit Energy");
hVar->GetXaxis()->SetTitle("Log10(Energy)(GeV)");
float outlier = hVar->Integral(57,-1);
float tot = hVar->Integral(0,-1);
float ratio = outlier/tot;
TString soutlier = "#geq 70MeV(100MIPs):"+std::to_string(ratio);
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
}
}


}
