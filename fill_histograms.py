#!/usr/bin/env python

import os
import sys
from ROOT import *
from array import array

GeV = 1.
TeV = 1e3

gROOT.SetBatch(1)

filelistname = sys.argv[1]

n_events_max = -1
if len(sys.argv) > 2:
    n_events_max = int(sys.argv[2])

tree_name = "nominal"
tree = TChain(tree_name, tree_name)
f = open(filelistname, 'r')
for fname in f.readlines():
    fname = fname.strip()
    tree.AddFile(fname)
n_entries = tree.GetEntries()
print "INFO: entries found:", n_entries

outfilename = "histograms/histograms." + \
    filelistname.split("/")[-1].replace(".txt", ".root")
outfile = TFile.Open(outfilename, "RECREATE")

_h = {}
_h['ljet1_px'] = TH1F(
    "ljet1_px", ";Leading large-R jet p_{x} [GeV];Events / Bin Width", 50, -500, 500)
_h['ljet1_py'] = TH1F(
    "ljet1_py", ";Leading large-R jet p_{y} [GeV];Events / Bin Width", 50, -500, 500)
_h['ljet1_pz'] = TH1F(
    "ljet1_pz", ";Leading large-R jet p_{z} [GeV];Events / Bin Width", 60, -1500, 1500)
_h['ljet1_pt'] = TH1F(
    "ljet1_pt", ";Leading large-R jet p_{T} [GeV];Events / Bin Width", 40,  200.,  800)
_h['ljet1_eta'] = TH1F(
    "ljet1_eta", ";Leading large-R jet #eta;Events / Bin Width", 40, -2.0, 2.0)
_h['ljet1_phi'] = TH1F(
    "ljet1_phi", ";Leading large-R jet #phi;Events / Bin Width", 32, -3.1415, 3.1415)
_h['ljet1_E'] = TH1F(
    "ljet1_E",  ";Leading large-R jet E [GeV];Events / Bin Width", 50, 0., 1500)
_h['ljet1_m'] = TH1F(
    "ljet1_m",  ";Leading large-R jet m [GeV];Events / Bin Width", 40, 0., 200.)

_h['ljet2_px'] = TH1F(
    "ljet2_px", ";2nd leading large-R jet p_{x} [GeV];Events / Bin Width", 50, -500, 500)
_h['ljet2_py'] = TH1F(
    "ljet2_py", ";2nd leading large-R jet p_{y} [GeV];Events / Bin Width", 50, -500, 500)
_h['ljet2_pz'] = TH1F(
    "ljet2_pz", ";2nd leading large-R jet p_{z} [GeV];Events / Bin Width", 60, -1500, 1500)
_h['ljet2_pt'] = TH1F(
    "ljet2_pt", ";2nd leading large-R jet p_{T} [GeV];Events / Bin Width", 40,   200., 600)
_h['ljet2_eta'] = TH1F(
    "ljet2_eta", ";2nd leading large-R jet #eta;Events / Bin Width", 40, -2.0, 2.0)
_h['ljet2_phi'] = TH1F(
    "ljet2_phi", ";2nd leading large-R jet #phi;Events / Bin Width", 32, -3.1415, 3.1415)
_h['ljet2_E'] = TH1F(
    "ljet2_E",  ";2nd leading large-R jet E [GeV];Events / Bin Width", 50, 0., 1500)
_h['ljet2_m'] = TH1F(
    "ljet2_m",  ";2nd leading large-R jet m [GeV];Events / Bin Width", 40, 0., 200.)

_h['jj_px'] = TH1F(
    "jj_px", ";Dijet system p_{x} [GeV];Events / Bin Width", 30, -300, 300)
_h['jj_py'] = TH1F(
    "jj_py", ";Dijet system p_{y} [GeV];Events / Bin Width", 30, -300, 300)
_h['jj_pz'] = TH1F(
    "jj_pz", ";Dijet system p_{z} [GeV];Events / Bin Width", 40, -2000, 2000)
_h['jj_pt'] = TH1F(
    "jj_pt", ";Dijet system p_{T} [GeV];Events / Bin Width", 30,    0., 300)
_h['jj_eta'] = TH1F(
    "jj_eta", ";Dijet system #eta;Events / Bin Width", 60, -6.0, 6.0)
_h['jj_phi'] = TH1F(
    "jj_phi", ";Dijet system #phi;Events / Bin Width", 32, -3.1415, 3.1415)
_h['jj_E'] = TH1F(
    "jj_E",  ";Dijet system E [GeV];Events / Bin Width", 30, 0., 3000)
_h['jj_m'] = TH1F(
    "jj_m",  ";Dijet system m [GeV];Events / Bin Width", 40, 0., 2000.)
_h['jj_dPhi'] = TH1F(
    "jj_dPhi", ";Dijet system #Delta#phi;Events / Bin Width", 32, 0, 3.1415)
_h['jj_dEta'] = TH1F(
    "jj_dEta", ";Dijet system #Delta#eta;Events / Bin Width", 30, -3., 3.)
_h['jj_dR'] = TH1F(
    "jj_dR",   ";Dijet system #Delta R;Events / Bin Width",   60, 2., 5)

_h['ljet1_E_vs_pt'] = TH2F(
    "ljet1_E_vs_pt",  ";Leading large-R jet p_{T} [GeV];Leading large-R jet E [GeV]", 40, 200., 800., 50, 0., 2000)
_h['ljet1_m_vs_pt'] = TH2F(
    "ljet1_m_vs_pt",  ";Leading large-R jet p_{T} [GeV];Leading large-R jet m [GeV]", 40, 200., 800., 40, 0., 200.)
_h['ljet1_m_vs_eta'] = TH2F(
    "ljet1_m_vs_eta", ";Leading large-R jet #eta;Leading large-R jet m [GeV]", 40, -2.0, 2.0, 30, 0., 600.)

_h['ljet2_E_vs_pt'] = TH2F(
    "ljet2_E_vs_pt",  ";2nd leading large-R jet p_{T} [GeV];2nd leading large-R jet E [GeV]", 40, 200., 800, 50, 0, 2000)
_h['ljet2_m_vs_pt'] = TH2F(
    "ljet2_m_vs_pt",  ";2nd leading large-R jet p_{T} [GeV];2nd leading large-R jet m [GeV]", 40, 200., 800, 40, 0., 200.)
_h['ljet2_m_vs_eta'] = TH2F(
    "ljet2_m_vs_eta", ";2nd leading large-R jet #eta;2nd leading large-R jet m [GeV]", 40, -2.0, 2.0, 40, 0., 200.)

_h['ljet2_pt_vs_ljet1_pt'] = TH2F(
    "ljet1_pt_vs_ljet2_pt", ";Leading large-R jet p_{T} [GeV];2nd leading large-R jet p_{T} [GeV]", 40, 200, 800, 40, 200, 800.)
_h['ljet2_m_vs_ljet1_m'] = TH2F(
    "ljet2_m_vs_ljet1_m",   ";Leading large-R jet m [GeV];2nd leading large-R jet m [GeV]", 40, 0., 200., 40, 0., 200.)
_h['ljet2_eta_vs_ljet1_eta'] = TH2F(
    "ljet2_eta_vs_ljet1_eta", ";Leading large-R jet #eta;2nd leading large-R jet #eta", 20, 0, 2.0, 20, 0, 2.0)

_h['jj_dR_vs_jj_m'] = TH2F(
    "jj_dR_vs_jj_m", ";Dijet system mass [GeV];Dijet system #Delta R",  80, 0., 4000., 60, 2., 5)
_h['jj_m_vs_jj_pt'] = TH2F(
    "jj_m_vs_jj_pt", ";Dijet system p_{T} [GeV];Dijet system mass [GeV]", 40,    0., 800, 80, 0., 4000.)
_h['ljet1_pt_vs_jj_m'] = TH2F(
    "ljet1_pt_vs_jj_m", ";Dijet system m [GeV];Leading large-R jet p_{T} [GeV];", 80, 0., 4000., 40,   200., 800)
_h['ljet2_pt_vs_jj_m'] = TH2F(
    "ljet2_pt_vs_jj_m", ";Dijet system m [GeV];2nd leading large-R jet p_{T} [GeV];", 80, 0., 4000., 40,   200., 800)

for h in _h.values():
    h.Sumw2()

if n_events_max > 0:
    n_entries = min(n_events_max, n_entries)
print "INFO: starting event loop:", n_entries

for ientry in range(n_entries):

    if (n_entries < 10) or ((ientry+1) % int(float(n_entries)/10.) == 0):
        perc = 100. * ientry / float(n_entries)
        print "INFO: Event %-9i  (%3.0f %%)" % (ientry, perc)

    tree.GetEntry(ientry)

    w = 1.0
    # w = tree.

    ljets = [TLorentzVector(), TLorentzVector()]
    lj1 = ljets[0]
    lj2 = ljets[1]

    lj1.SetPtEtaPhiM(tree.ljet1_pt,
                     tree.ljet1_eta,
                     tree.ljet1_phi,
                     tree.ljet1_m)

    lj2.SetPtEtaPhiM(tree.ljet2_pt,
                     tree.ljet2_eta,
                     tree.ljet2_phi,
                     tree.ljet2_m)

#    if lj1.Pt() < 500*GeV: continue
#    if lj2.Pt() < 350*GeV: continue

    jj = lj1 + lj2
    jj.dPhi = lj1.DeltaPhi(lj2)
    jj.dEta = lj1.Eta() - lj2.Eta()
    jj.dR = lj1.DeltaR(lj2)

    #abcd16 = tree.abcd16

    _h['ljet1_px'].Fill(lj1.Px()/GeV, w)
    _h['ljet1_py'].Fill(lj1.Py()/GeV, w)
    _h['ljet1_pz'].Fill(lj1.Pz()/GeV, w)
    _h['ljet1_pt'].Fill(lj1.Pt()/GeV, w)
    _h['ljet1_eta'].Fill(lj1.Eta(), w)
    _h['ljet1_phi'].Fill(lj1.Phi(), w)
    _h['ljet1_E'].Fill(lj1.E()/GeV, w)
    _h['ljet1_m'].Fill(lj1.M()/GeV, w)

    _h['ljet2_px'].Fill(lj2.Px()/GeV, w)
    _h['ljet2_py'].Fill(lj2.Py()/GeV, w)
    _h['ljet2_pz'].Fill(lj2.Pz()/GeV, w)
    _h['ljet2_pt'].Fill(lj2.Pt()/GeV, w)
    _h['ljet2_eta'].Fill(lj2.Eta(), w)
    _h['ljet2_phi'].Fill(lj2.Phi(), w)
    _h['ljet2_E'].Fill(lj2.E()/GeV, w)
    _h['ljet2_m'].Fill(lj2.M()/GeV, w)

    _h['jj_px'].Fill(jj.Px()/GeV, w)
    _h['jj_py'].Fill(jj.Py()/GeV, w)
    _h['jj_pz'].Fill(jj.Pz()/GeV, w)
    _h['jj_pt'].Fill(jj.Pt()/GeV, w)
    _h['jj_eta'].Fill(jj.Eta(), w)
    _h['jj_phi'].Fill(jj.Phi(), w)
    _h['jj_E'].Fill(jj.E()/GeV, w)
    _h['jj_m'].Fill(jj.M()/GeV, w)
    _h['jj_dPhi'].Fill(abs(jj.dPhi), w)
    _h['jj_dEta'].Fill(jj.dEta, w)
    _h['jj_dR'].Fill(jj.dR, w)

    _h['ljet1_E_vs_pt'].Fill(lj1.Pt()/GeV, lj1.E()/GeV, w)
    _h['ljet1_m_vs_pt'].Fill(lj1.Pt()/GeV, lj1.M()/GeV, w)
    _h['ljet1_m_vs_eta'].Fill(lj1.Eta(),    lj1.M()/GeV, w)

    _h['ljet2_E_vs_pt'].Fill(lj2.Pt()/GeV, lj2.E()/GeV, w)
    _h['ljet2_m_vs_pt'].Fill(lj2.Pt()/GeV, lj2.M()/GeV, w)
    _h['ljet2_m_vs_eta'].Fill(lj2.Eta(),    lj2.M()/GeV, w)

    _h['ljet2_pt_vs_ljet1_pt'].Fill(lj1.Pt()/GeV, lj2.Pt()/GeV, w)
    _h['ljet2_m_vs_ljet1_m'].Fill(lj1.M()/GeV, lj2.M()/GeV, w)
    _h['ljet2_eta_vs_ljet1_eta'].Fill(abs(lj1.Eta()), abs(lj2.Eta()), w)

    _h['jj_dR_vs_jj_m'].Fill(jj.M()/GeV, jj.dR, w)
    _h['jj_m_vs_jj_pt'].Fill(jj.Pt()/GeV, jj.M()/GeV, w)
    _h['ljet1_pt_vs_jj_m'].Fill(jj.M()/GeV, lj1.Pt()/GeV, w)
    _h['ljet2_pt_vs_jj_m'].Fill(jj.M()/GeV, lj2.Pt()/GeV, w)


outfile.Write()
outfile.Close()
print "INFO: Create output file:", outfile.GetName()
