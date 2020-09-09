"""MaterialsCoord package for benchmarking crystal structure bonding algorithms."""

__version__ = "0.2.0"

structure_mapping = {
    # elemental mapping
    "As_alpha_16518": "$\\alpha$-As",
    "C_diamond_52054": "C (diamond)",
    "C_graphite_76767": "C (graphite)",
    "Cu_52256": "Cu",
    "Ga_12174": "Ga (III)",
    "Hg_alpha_104296": "$\\alpha$-Hg",
    "La_43573": "La",
    "Mg_52260": "Mg",
    "Mn_alpha_42743": "$\\alpha$-Mn",
    "Mn_beta_41775": "$\\beta$-Mn",
    "P_black_23836": "P (black)",
    "Se_trigonal_23068": "Se (trigonal)",
    "Sm_76031": "Sm",
    "Sn_beta_106072": "$\\beta$-Sn",
    "U_alpha_16056": "$\\alpha$-U",
    "W_alpha_43667": "$\\alpha$-W",
    # common_binaries mapping
    "Al2O3_corundum_9770": "Al$_2$O$_3$ (corundum)",
    "CsCl_53847": "CsCl",
    "Cu5Zn8_gamma_brass_2092": "Cu$_5$Zn$_8$ ($\\gamma$-brass)",
    "Fe3O4_inv_spinel_26410": "Fe$_3$O$_4$",
    "NaCl_rocksalt_100633": "NaCl (rock-salt)",
    "NiAs_5245": "NiAs",
    "Pb3O4_22325": "Pb$_3$O$_4$",
    "Th3P4_25724": "Th$_3$P$_4$",
    "TiO2_rutile_9852": "TiO$_2$ (rutile)",
    "ZnS_sphalerite_651455": "ZnS (sphalerite)",
    "ZnS_wurtzite_67453": "ZnS (wurtzite)",
    # ABX3 mapping
    "BaTiO3_67520": "BaTiO$_3$",
    "CaCO3_aragonite_15194": "CaCO$_3$ (aragonite)",
    "CaCO3_calcite_18164": "CaCO$_3$ (calcite)",
    "FeTiO3_ilmenite_9805": "FeTiO$_3$",
    "SrTiO3_perovskite_80871": "SrTiO$_3$",
    # ABX4 mapping
    "AlAsO4_33254": "AlAsO$_4$",
    "BAsO4_highcristobalite_26891": "BAsO$_4$",
    "BaAl2O4_21080": "BaAl$_2$O$_4$",
    "BaZnF4_182604": "BaZnF$_4$",
    "CaFe2O4_166080": "CaFe$_2$O$_4$",
    "CaWO4_scheelite_15586": "CaWO$_4$",
    "CePO4_monazite_79746": "CePO$_4$",
    "CrVO4_27508": "CrVO$_4$",
    "FeWO4_wolframite_26811": "FeWO$_4$",
    "GaPO4_lowcristobalite_97550": "GaPO$_4$",
    "MgUO4_24725": "MgUO$_4$",
    "MnMoO4_alpha_15615": "MnMoO$_4$",
    "SbNbO4_20344": "SbNbO$_4$",
    "TlAlF4_202453": "TlAlF$_4$",
    "ZnSO4_71018": "ZnSO$_4$",
    "ZrSiO4_zircon_15759": "ZrSiO$_4$",
    # A2BX4 mapping
    "Be2SiO4_phenakite_64942": "Be$_2$SiO$_4$",
    "CaB2O4_34641": "CaB$_2$O$_4$",
    "Fe2SiO4_olivine_4353": "Fe$_2$SiO$_4$",
    "K2NiF4_73450": "K$_2$NiF$_4$",
    "K2SO4_beta_2827": "K$_2$SO$_4$",
    "MgAl2O4_spinel_31373": "MgAl$_2$O$_4$",
    "Na2SO4_thenardite_2895": "Na$_2$SO$_4$",
    "Sr2PbO4_16806": "Sr$_2$PbO$_4$",
    # intermetallic mapping
    "AgMgSb_259186": "AgMgSb",
    "AlB2_606058": "AlB$_2$",
    "CaCu5_619215": "CaCu$_5$",
    "CaIn2_58686": "CaIn$_2$",
    "CeAl2Ga2_606460": "CeAl$_2$Ga$_2$",
    "KHg2_104303": "KHg$_2$",
    "MgCu2_46007": "MgCu$_2$",
    "MgZn2_46006": "MgZn$_2$",
    "Mn5Si3_166772": "Mn$_5$Si$_3$",
    "MnCu2Al_607010": "MnCu$_2$Al",
    "Mo2FeB2_5431": "Mo$_2$FeB$_2$",
    "Th2Zn17_653256": "Th$_2$Zn$_{17}$",
    "ThMn12_104986": "ThMn$_{12}$",
    "TiNiSi_18188": "TiNiSi",
    "ZrNiAl_152131": "ZrNiAl"
}
