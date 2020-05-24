#include <math.h>
#include <string>
#include <iostream>
#include <dirent.h>

using namespace std;
void Cversion(){

TCanvas* c1 = new TCanvas( "c1", "Histogram Drawing Options", 800,800 );
c1->SetGrid();
gStyle->SetHistLineWidth(3);
gStyle->SetLineWidth(3);
gPad->SetTickx();
gPad->SetTicky();
gStyle->SetLineWidth(3);
gStyle->SetPalette(kBird);
gStyle->SetOptStat(1000111);
gStyle->SetStatW(0.18);
gStyle->SetStatH(0.18);
c1->Clear();
TPad* pad1 = new TPad("pad1", "The pad with the function",0,0.25,1,1);
pad1->SetFrameLineWidth(3);


pad1->Draw();
c1->cd();
vector<string> filelist;
const char *path = "/eos/uscms/store/group/lpchbb/LLDJntuples/SuhoKim_Ntuples/ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10_TuneCUETP8M1_13TeV-powheg-pythia8/crab_ZH_HToSSTobbbb_MS-15_ctauS-10/190516_043325/0000/";
string sample ="ZH_HToSSTobbbb_ZToLL_MH-125_MS-15_ctauS-10 & 5";
TH1F* h16 = new TH1F("Decaydist","Decaydist",10, 0, 10);
TH1F* h16w = new TH1F("Run","Run",10, 0, 10);
h16w->Sumw2();
TH1F* h16s = new TH1F("ctauEventWeight","ctauEventWeight",80, 0, 4);
DIR *dir;
struct dirent *ent;
if ((dir = opendir (path)) != NULL) {
  /* print all the files and directories within directory */
  while ((ent = readdir (dir)) != NULL) {
    printf ("%s%s\n",path,ent->d_name);
    string subname = ent->d_name;
    string filename = path + subname;
    //std::cout<<filename<<std::endl;
    filelist.push_back(filename);
  }
  closedir (dir);
}
for (int j=2; j<(int)filelist.size(); ++j)
{cout<<filelist[j]<<endl;} 
vector<float> *ctauEventWeight;
Int_t Run;

for (int j=2; j<(int)filelist.size(); ++j){
        string conname = filelist[j];
	const char *filename = conname.c_str();
        TFile* _file0 = TFile::Open(filename,"read");
	TTree* mytree16 = (TTree*)_file0->Get("lldjNtuple/EventTree");
	//mytree16->Print();
	
	mytree16->SetBranchAddress("ctauEventWeight",&ctauEventWeight);
        mytree16->SetBranchAddress("run",&Run);
	for (int i =0; i<(int)mytree16->GetEntries(); ++i){
	//	//h16s.Fill(ctau[0],1);
	//	//print(ctau[0])
		mytree16->GetEntry(i);	
		h16->Fill(Run,1);
		//cout<<ctauEventWeight->at(0)<<endl;
		h16w->Fill(Run,ctauEventWeight->at(0));
	//	
	//	//Decaydist=mytree16.Decaydist
	//	//weight = mytree16.Simweight
	//	//number = Decaydist.size()
	//	//for i in range(number):
	//	//	#h16s.Fill(weight[i],1)
	//	//	h16.Fill(Decaydist[i],1)
	//	//	h16w.Fill(Decaydist[i],weight[i])
	}}	
Double_t error;
Double_t integral = h16w->IntegralAndError(0, h16w->GetNbinsX(), error, ""); // "" ... or ... "width"
std::cout << "Hist integral = " << h16w->Integral() << " +- " << error << std::endl;
//IntError=h16w.IntegralAndError(1,h16w.GetNbinsX(),error,"");
//print(error)
h16w->Draw("HIST");
h16w->SetLineColor(4);
h16->Draw("HIST SAME");
//h16->GetXaxis()->SetTitle("Decay distance in scalar frame")
h16w->GetYaxis()->SetRangeUser(0,50010);
h16->SetLineColor(2);

//str2='#int_{10mm} ='+str(h16.Integral())
//str1='#int_{5mm} ='+str(h16w.Integral())
//str3='Normalization = '+str(h16w.Integral()/h16.Integral())
TLegend *legend = new TLegend(0.5,0.75,0.7,0.9); 		
legend->AddEntry(h16,"Decaydist for c#tau =10mm","f");
legend->AddEntry(h16w,"Decaydist for c#tau =5mm","f");
legend->Draw();
TPaveText *fitbox = new TPaveText(.3,.75,.5,.9,"brNDC");
fitbox->SetBorderSize(1);
fitbox->SetFillColor(0);
fitbox->AddText("#int_{5mm} = 48544.5 +- 292.406");
fitbox->AddText("#int_{10mm} = 50000");
fitbox->AddText("Normalization = 0.970889");
fitbox->Draw();
TLatex *l = new TLatex();
l->SetTextAlign(13);
l->SetTextSize(0.02);
l->DrawLatexNDC(0.23,0.92,"CMS #it{Preliminary}                           Eras GH    16.2/fb  (13TeV)");
c1->Modified();
c1->Update();
c1->SaveAs("1w.png");








//c2 = TCanvas( 'c2', 'Histogram Drawing Options', 800,800 )
//gStyle.SetHistLineWidth(3)
//gPad.SetTickx()
//gPad.SetTicky()
//h16s.Draw('HIST')
//#h16s.Fit("expo")
//h16s.SetTitle('EvenWeight for ctau 10mm->5mm')
//h16s.GetXaxis().SetTitle('EventWeight')
//l = TLatex()
//l.SetTextAlign(13)
//l.SetTextSize(0.02)
//l.DrawLatexNDC(0.23,0.92,"CMS #it{Preliminary}                           Eras GH    16.2/fb  (13TeV)")
//c2.Modified()
//c2.Update()
//c2.SaveAs("2w.png")
}


