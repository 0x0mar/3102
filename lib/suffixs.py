#!/usr/bin/env python
# coding=utf-8

"""
Copyright (c) 2014 Fooying (http://www.fooying.com)
Mail:f00y1n9[at]gmail.com

收集的所有域名后缀
"""

SUFFIXS = set([
    "ac",
    "ad",
    "ae",
    "aero",
    "af",
    "ag",
    "ai",
    "al",
    "am",
    "an",
    "ao",
    "aq",
    "ar",
    "arpa",
    "as",
    "at",
    "au",
    "aw",
    "ax",
    "az",
    "ba",
    "bb",
    "bd",
    "be",
    "bf",
    "bg",
    "bh",
    "bi",
    "biz",
    "bj",
    "bm",
    "bn",
    "bo",
    "br",
    "bs",
    "bt",
    "bv",
    "bw",
    "by",
    "bz",
    "ca",
    "cat",
    "cc",
    "cd",
    "cf",
    "cg",
    "ch",
    "ck",
    "cl",
    "cm",
    "cn",
    "co",
    "com",
    "coop",
    "cr",
    "cu",
    "cv",
    "cx",
    "cy",
    "cz",
    "de",
    "dj",
    "dk",
    "dm",
    "do",
    "dz",
    "ec",
    "edu",
    "ee",
    "eg",
    "er",
    "es",
    "et",
    "eu",
    "fi",
    "fj",
    "fk",
    "fm",
    "fo",
    "fr",
    "ga",
    "gb",
    "gd",
    "ge",
    "gf",
    "gg",
    "gh",
    "gi",
    "gl",
    "gm",
    "gn",
    "gov",
    "gp",
    "gq",
    "gr",
    "gs",
    "gt",
    "gu",
    "gw",
    "gy",
    "hk",
    "hm",
    "hn",
    "hr",
    "ht",
    "hu",
    "id",
    "ie",
    "il",
    "im",
    "in",
    "info",
    "int",
    "io",
    "iq",
    "ir",
    "is",
    "it",
    "je",
    "jm",
    "jo",
    "jobs",
    "jp",
    "ke",
    "kg",
    "kh",
    "ki",
    "km",
    "kn",
    "kr",
    "kw",
    "ky",
    "kz",
    "la",
    "lb",
    "lc",
    "li",
    "lk",
    "lr",
    "ls",
    "lt",
    "lu",
    "lv",
    "ly",
    "ma",
    "mc",
    "md",
    "mg",
    "mh",
    "mil",
    "mk",
    "ml",
    "mm",
    "mn",
    "mo",
    "mobi",
    "mp",
    "mq",
    "mr",
    "ms",
    "mt",
    "mu",
    "museum",
    "mv",
    "mw",
    "mx",
    "my",
    "mz",
    "na",
    "name",
    "nc",
    "ne",
    "net",
    "nf",
    "ng",
    "ni",
    "nl",
    "no",
    "np",
    "nr",
    "nu",
    "nz",
    "om",
    "org",
    "pa",
    "pe",
    "pf",
    "pg",
    "ph",
    "pk",
    "pl",
    "pm",
    "pn",
    "pr",
    "pro",
    "ps",
    "pt",
    "pw",
    "py",
    "qa",
    "re",
    "ro",
    "ru",
    "rw",
    "sa",
    "sb",
    "sc",
    "sd",
    "se",
    "sg",
    "sh",
    "si",
    "sj",
    "sk",
    "sl",
    "sm",
    "sn",
    "so",
    "sr",
    "st",
    "su",
    "sv",
    "sy",
    "sz",
    "tc",
    "td",
    "tf",
    "tg",
    "th",
    "tj",
    "tk",
    "tl",
    "tm",
    "tn",
    "to",
    "tp",
    "tr",
    "travel",
    "tt",
    "tv",
    "tw",
    "tz",
    "ua",
    "ug",
    "uk",
    "um",
    "us",
    "uy",
    "uz",
    "va",
    "vc",
    "ve",
    "vg",
    "vi",
    "vn",
    "vu",
    "wf",
    "ws",
    "ye",
    "yt",
    "yu",
    "za",
    "zm",
    "zw",
    "asia",
    "eh",
    "kp",
    "me",
    "rs",
    "tel",
    "com.ac",
    "edu.ac",
    "gov.ac",
    "net.ac",
    "mil.ac",
    "org.ac",
    "ad",
    "nom.ad",
    "ae",
    "net.ae",
    "gov.ae",
    "org.ae",
    "mil.ae",
    "sch.ae",
    "ac.ae",
    "pro.ae",
    "name.ae",
    "aero",
    "af",
    "gov.af",
    "edu.af",
    "net.af",
    "com.af",
    "ag",
    "com.ag",
    "org.ag",
    "net.ag",
    "co.ag",
    "nom.ag",
    "ai",
    "off.ai",
    "com.ai",
    "net.ai",
    "org.ai",
    "gov.al",
    "edu.al",
    "org.al",
    "com.al",
    "net.al",
    "uniti.al",
    "tirana.al",
    "soros.al",
    "upt.al",
    "inima.al",
    "am",
    "an",
    "com.an",
    "net.an",
    "org.an",
    "edu.an",
    "co.ao",
    "ed.ao",
    "gv.ao",
    "it.ao",
    "og.ao",
    "pb.ao",
    "com.ar",
    "gov.ar",
    "int.ar",
    "mil.ar",
    "net.ar",
    "org.ar",
    "e164.arpa",
    "in-addr.arpa",
    "iris.arpa",
    "ip6.arpa",
    "uri.arpa",
    "urn.arpa",
    "as",
    "at",
    "gv.at",
    "ac.at",
    "co.at",
    "or.at",
    "priv.at",
    "asn.au",
    "com.au",
    "net.au",
    "id.au",
    "org.au",
    "csiro.au",
    "oz.au",
    "info.au",
    "conf.au",
    "act.au",
    "nsw.au",
    "nt.au",
    "qld.au",
    "sa.au",
    "tas.au",
    "vic.au",
    "wa.au",
    "aw",
    "com.aw",
    "ax",
    "az",
    "com.az",
    "net.az",
    "int.az",
    "gov.az",
    "biz.az",
    "org.az",
    "edu.az",
    "mil.az",
    "pp.az",
    "name.az",
    "info.az",
    "com.bb",
    "edu.bb",
    "gov.bb",
    "net.bb",
    "org.bb",
    "com.bd",
    "edu.bd",
    "net.bd",
    "gov.bd",
    "org.bd",
    "mil.bd",
    "ac.be",
    "gov.bf",
    "possibly",
    "com.bm",
    "edu.bm",
    "org.bm",
    "gov.bm",
    "net.bm",
    "com.bn",
    "edu.bn",
    "org.bn",
    "net.bn",
    "bo",
    "com.bo",
    "org.bo",
    "net.bo",
    "gov.bo",
    "gob.bo",
    "edu.bo",
    "tv.bo",
    "mil.bo",
    "int.bo",
    "agr.br",
    "am.br",
    "art.br",
    "edu.br",
    "com.br",
    "coop.br",
    "esp.br",
    "far.br",
    "fm.br",
    "g12.br",
    "gov.br",
    "imb.br",
    "ind.br",
    "inf.br",
    "mil.br",
    "net.br",
    "org.br",
    "psi.br",
    "rec.br",
    "srv.br",
    "tmp.br",
    "tur.br",
    "tv.br",
    "etc.br",
    "adm.br",
    "adv.br",
    "arq.br",
    "ato.br",
    "bio.br",
    "bmd.br",
    "cim.br",
    "cng.br",
    "cnt.br",
    "ecn.br",
    "eng.br",
    "eti.br",
    "fnd.br",
    "fot.br",
    "fst.br",
    "ggf.br",
    "jor.br",
    "lel.br",
    "mat.br",
    "med.br",
    "mus.br",
    "not.br",
    "ntr.br",
    "odo.br",
    "ppg.br",
    "pro.br",
    "psc.br",
    "qsl.br",
    "slg.br",
    "trd.br",
    "vet.br",
    "zlg.br",
    "dpn.br",
    "nom.br",
    "bs",
    "com.bs",
    "net.bs",
    "org.bs",
    "bt",
    "com.bt",
    "edu.bt",
    "gov.bt",
    "net.bt",
    "org.bt",
    "bw",
    "co.bw",
    "org.bw",
    "gov.by",
    "mil.by",
    "ca",
    "ab.ca",
    "bc.ca",
    "mb.ca",
    "nb.ca",
    "nf.ca",
    "nl.ca",
    "ns.ca",
    "nt.ca",
    "nu.ca",
    "on.ca",
    "pe.ca",
    "qc.ca",
    "sk.ca",
    "yk.ca",
    "cc",
    "co.cc",
    "cd",
    "com.cd",
    "net.cd",
    "org.cd",
    "ch",
    "com.ch",
    "net.ch",
    "org.ch",
    "gov.ch",
    "co.ck",
    "and",
    "cn",
    "ac.cn",
    "com.cn",
    "edu.cn",
    "gov.cn",
    "net.cn",
    "org.cn",
    "ah.cn",
    "bj.cn",
    "cq.cn",
    "fj.cn",
    "gd.cn",
    "gs.cn",
    "gz.cn",
    "gx.cn",
    "ha.cn",
    "hb.cn",
    "he.cn",
    "hi.cn",
    "hl.cn",
    "hn.cn",
    "jl.cn",
    "js.cn",
    "jx.cn",
    "ln.cn",
    "nm.cn",
    "nx.cn",
    "qh.cn",
    "sc.cn",
    "sd.cn",
    "sh.cn",
    "sn.cn",
    "sx.cn",
    "tj.cn",
    "xj.cn",
    "xz.cn",
    "yn.cn",
    "zj.cn",
    "com.co",
    "edu.co",
    "org.co",
    "gov.co",
    "mil.co",
    "net.co",
    "nom.co",
    "ac.cr",
    "co.cr",
    "ed.cr",
    "fi.cr",
    "go.cr",
    "or.cr",
    "sa.cr",
    "cu",
    "com.cu",
    "edu.cu",
    "org.cu",
    "net.cu",
    "gov.cu",
    "inf.cu",
    "cx",
    "gov.cx",
    "com.cy",
    "biz.cy",
    "info.cy",
    "ltd.cy",
    "pro.cy",
    "net.cy",
    "org.cy",
    "name.cy",
    "tm.cy",
    "ac.cy",
    "ekloges.cy",
    "press.cy",
    "parliament.cy",
    "dm",
    "com.dm",
    "net.dm",
    "org.dm",
    "edu.dm",
    "gov.dm",
    "edu.do",
    "gov.do",
    "gob.do",
    "com.do",
    "org.do",
    "sld.do",
    "web.do",
    "net.do",
    "mil.do",
    "art.do",
    "dz",
    "com.dz",
    "org.dz",
    "net.dz",
    "gov.dz",
    "edu.dz",
    "asso.dz",
    "pol.dz",
    "art.dz",
    "ec",
    "com.ec",
    "info.ec",
    "net.ec",
    "fin.ec",
    "med.ec",
    "pro.ec",
    "org.ec",
    "edu.ec",
    "gov.ec",
    "mil.ec",
    "ee",
    "com.ee",
    "org.ee",
    "fie.ee",
    "pri.ee",
    "eun.eg",
    "edu.eg",
    "sci.eg",
    "gov.eg",
    "com.eg",
    "org.eg",
    "net.eg",
    "mil.eg",
    "es",
    "com.es",
    "nom.es",
    "org.es",
    "gob.es",
    "edu.es",
    "com.et",
    "gov.et",
    "org.et",
    "edu.et",
    "net.et",
    "biz.et",
    "name.et",
    "info.et",
    "fi",
    "aland.fi",
    "biz.fj",
    "com.fj",
    "info.fj",
    "name.fj",
    "net.fj",
    "org.fj",
    "pro.fj",
    "ac.fj",
    "gov.fj",
    "mil.fj",
    "school.fj",
    "co.fk",
    "org.fk",
    "gov.fk",
    "ac.fk",
    "nom.fk",
    "net.fk",
    "fr",
    "tm.fr",
    "asso.fr",
    "nom.fr",
    "prd.fr",
    "presse.fr",
    "com.fr",
    "gouv.fr",
    "ge",
    "com.ge",
    "edu.ge",
    "gov.ge",
    "org.ge",
    "mil.ge",
    "net.ge",
    "pvt.ge",
    "gg",
    "co.gg",
    "net.gg",
    "org.gg",
    "com.gh",
    "edu.gh",
    "gov.gh",
    "org.gh",
    "mil.gh",
    "gi",
    "com.gi",
    "ltd.gi",
    "gov.gi",
    "mod.gi",
    "edu.gi",
    "org.gi",
    "com.gn",
    "ac.gn",
    "gov.gn",
    "org.gn",
    "net.gn",
    "gp",
    "com.gp,",
    "net.gp,",
    "edu.gp,",
    "asso.gp,",
    "or",
    "org.gp",
    "gr",
    "com.gr",
    "edu.gr",
    "net.gr",
    "org.gr",
    "gov.gr",
    "hk",
    "com.hk",
    "edu.hk",
    "gov.hk",
    "idv.hk",
    "net.hk",
    "org.hk",
    "hn",
    "com.hn",
    "edu.hn",
    "org.hn",
    "net.hn",
    "mil.hn",
    "gob.hn",
    "hr",
    "iz.hr",
    "from.hr",
    "name.hr",
    "com.hr",
    "ht",
    "com.ht",
    "net.ht",
    "firm.ht",
    "shop.ht",
    "info.ht",
    "pro.ht",
    "adult.ht",
    "org.ht",
    "art.ht",
    "pol.ht",
    "rel.ht",
    "asso.ht",
    "perso.ht",
    "coop.ht",
    "med.ht",
    "edu.ht",
    "gouv.ht",
    "hu",
    "co.hu",
    "info.hu",
    "org.hu",
    "priv.hu",
    "sport.hu",
    "tm.hu",
    "2000.hu",
    "agrar.hu",
    "bolt.hu",
    "casino.hu",
    "city.hu",
    "erotica.hu",
    "erotika.hu",
    "film.hu",
    "forum.hu",
    "games.hu",
    "hotel.hu",
    "ingatlan.hu",
    "jogasz.hu",
    "konyvelo.hu",
    "lakas.hu",
    "media.hu",
    "news.hu",
    "reklam.hu",
    "sex.hu",
    "shop.hu",
    "suli.hu",
    "szex.hu",
    "tozsde.hu",
    "utazas.hu",
    "video.hu",
    "ac.id",
    "co.id",
    "or.id",
    "go.id",
    "ie",
    "gov.ie",
    "ac.il",
    "co.il",
    "org.il",
    "net.il",
    "k12.il",
    "gov.il",
    "muni.il",
    "idf.il",
    "co.im",
    "ltd.co.im",
    "plc.co.im",
    "net.im",
    "gov.im",
    "org.im",
    "nic.im",
    "ac.im",
    "in",
    "co.in",
    "firm.in",
    "net.in",
    "org.in",
    "gen.in",
    "ind.in",
    "nic.in",
    "ac.in",
    "edu.in",
    "res.in",
    "gov.in",
    "mil.in",
    "ir",
    "ac.ir",
    "co.ir",
    "gov.ir",
    "net.ir",
    "org.ir",
    "sch.ir",
    "it",
    "gov.it",
    "je",
    "co.je",
    "net.je",
    "org.je",
    "edu.jm",
    "gov.jm",
    "com.jm",
    "net.jm",
    "org.jm",
    "jo",
    "com.jo",
    "org.jo",
    "net.jo",
    "edu.jo",
    "gov.jo",
    "mil.jo",
    "jp",
    "ac.jp",
    "ad.jp",
    "co.jp",
    "ed.jp",
    "go.jp",
    "gr.jp",
    "lg.jp",
    "ne.jp",
    "or.jp",
    "per.kh",
    "com.kh",
    "edu.kh",
    "gov.kh",
    "mil.kh",
    "net.kh",
    "org.kh",
    "kr",
    "co.kr",
    "or.kr",
    "com.kw",
    "edu.kw",
    "gov.kw",
    "net.kw",
    "org.kw",
    "mil.kw",
    "ky",
    "edu.ky",
    "gov.ky",
    "com.ky",
    "org.ky",
    "net.ky",
    "org.kz",
    "edu.kz",
    "net.kz",
    "gov.kz",
    "mil.kz",
    "com.kz",
    "net.lb",
    "org.lb",
    "gov.lb",
    "edu.lb",
    "com.lb",
    "com.lc",
    "org.lc",
    "edu.lc",
    "gov.lc",
    "li",
    "com.li",
    "net.li",
    "org.li",
    "gov.li",
    "lk",
    "gov.lk",
    "sch.lk",
    "net.lk",
    "int.lk",
    "com.lk",
    "org.lk",
    "edu.lk",
    "ngo.lk",
    "soc.lk",
    "web.lk",
    "ltd.lk",
    "assn.lk",
    "grp.lk",
    "hotel.lk",
    "com.lr",
    "edu.lr",
    "gov.lr",
    "org.lr",
    "net.lr",
    "org.ls",
    "co.ls",
    "lt",
    "gov.lt",
    "mil.lt",
    "lu",
    "gov.lu",
    "mil.lu",
    "org.lu",
    "net.lu",
    "lv",
    "com.lv",
    "edu.lv",
    "gov.lv",
    "org.lv",
    "mil.lv",
    "id.lv",
    "net.lv",
    "asn.lv",
    "conf.lv",
    "ly",
    "com.ly",
    "net.ly",
    "gov.ly",
    "plc.ly",
    "edu.ly",
    "sch.ly",
    "med.ly",
    "org.ly",
    "id.ly",
    "ma",
    "co.ma",
    "net.ma",
    "gov.ma",
    "org.ma",
    "mc",
    "tm.mc",
    "asso.mc",
    "mg",
    "org.mg",
    "nom.mg",
    "gov.mg",
    "prd.mg",
    "tm.mg",
    "com.mg",
    "edu.mg",
    "mil.mg",
    "army.mil",
    "navy.mil",
    "mk",
    "com.mk",
    "org.mk",
    "mo",
    "com.mo",
    "net.mo",
    "org.mo",
    "edu.mo",
    "gov.mo",
    "weather.mobi",
    "music.mobi",
    "mt",
    "org.mt",
    "com.mt",
    "gov.mt",
    "edu.mt",
    "net.mt",
    "mu",
    "com.mu",
    "co.mu",
    "aero.mv",
    "biz.mv",
    "com.mv",
    "coop.mv",
    "edu.mv",
    "gov.mv",
    "info.mv",
    "int.mv",
    "mil.mv",
    "museum.mv",
    "name.mv",
    "net.mv",
    "org.mv",
    "pro.mv",
    "ac.mw",
    "co.mw",
    "com.mw",
    "coop.mw",
    "edu.mw",
    "gov.mw",
    "int.mw",
    "museum.mw",
    "net.mw",
    "org.mw",
    "com.mx",
    "net.mx",
    "org.mx",
    "edu.mx",
    "gob.mx",
    "com.my",
    "net.my",
    "org.my",
    "gov.my",
    "edu.my",
    "mil.my",
    "name.my",
    "edu.ng",
    "com.ng",
    "gov.ng",
    "org.ng",
    "net.ng",
    "gob.ni",
    "com.ni",
    "edu.ni",
    "org.ni",
    "nom.ni",
    "net.ni",
    "nl",
    "000.nl",
    "999.nl",
    "no",
    "mil.no",
    "stat.no",
    "kommune.no",
    "herad.no",
    "priv.no",
    "vgs.no",
    "fhs.no",
    "museum.no",
    "fylkesbibl.no",
    "folkebibl.no",
    "idrett.no",
    "geo.no",
    "gs.county.no",
    "com.np",
    "org.np",
    "edu.np",
    "net.np",
    "gov.np",
    "mil.np",
    "nr",
    "gov.nr",
    "edu.nr",
    "biz.nr",
    "info.nr",
    "nr",
    "org.nr",
    "com.nr",
    "net.nr",
    "ac.nz",
    "co.nz",
    "cri.nz",
    "gen.nz",
    "geek.nz",
    "govt.nz",
    "iwi.nz",
    "maori.nz",
    "mil.nz",
    "net.nz",
    "org.nz",
    "school.nz",
    "com.om",
    "co.om",
    "edu.om",
    "ac.com",
    "sch.om",
    "gov.om",
    "net.om",
    "org.om",
    "mil.om",
    "museum.om",
    "biz.om",
    "pro.om",
    "med.om",
    "com.pa",
    "ac.pa",
    "sld.pa",
    "gob.pa",
    "edu.pa",
    "org.pa",
    "net.pa",
    "abo.pa",
    "ing.pa",
    "med.pa",
    "nom.pa",
    "com.pe",
    "org.pe",
    "net.pe",
    "edu.pe",
    "mil.pe",
    "gob.pe",
    "nom.pe",
    "pf",
    "com.pf",
    "org.pf",
    "edu.pf",
    "com.pg",
    "net.pg",
    "ph",
    "com.ph",
    "gov.ph",
    "pk",
    "com.pk",
    "net.pk",
    "edu.pk",
    "org.pk",
    "fam.pk",
    "biz.pk",
    "web.pk",
    "gov.pk",
    "gob.pk",
    "gok.pk",
    "gon.pk",
    "gop.pk",
    "gos.pk",
    "pl",
    "com.pl",
    "biz.pl",
    "net.pl",
    "art.pl",
    "edu.pl",
    "org.pl",
    "ngo.pl",
    "gov.pl",
    "info.pl",
    "mil.pl",
    "pr",
    "biz.pr",
    "com.pr",
    "edu.pr",
    "gov.pr",
    "info.pr",
    "isla.pr",
    "name.pr",
    "net.pr",
    "org.pr",
    "pro.pr",
    "law.pro",
    "med.pro",
    "cpa.pro",
    "ps",
    "edu.ps",
    "gov.ps",
    "sec.ps",
    "plo.ps",
    "com.ps",
    "org.ps",
    "net.ps",
    "pt",
    "com.pt",
    "edu.pt",
    "gov.pt",
    "int.pt",
    "net.pt",
    "nome.pt",
    "org.pt",
    "publ.pt",
    "net.py",
    "org.py",
    "gov.py",
    "edu.py",
    "com.py",
    "ro",
    "com.ro",
    "org.ro",
    "tm.ro",
    "nt.ro",
    "nom.ro",
    "info.ro",
    "rec.ro",
    "arts.ro",
    "firm.ro",
    "store.ro",
    "www.ro",
    "ru",
    "com.ru",
    "net.ru",
    "org.ru",
    "pp.ru",
    "msk.ru",
    "int.ru",
    "ac.ru",
    "rw",
    "gov.rw",
    "net.rw",
    "edu.rw",
    "ac.rw",
    "com.rw",
    "co.rw",
    "int.rw",
    "mil.rw",
    "gouv.rw",
    "com.sa",
    "edu.sa",
    "sch.sa",
    "med.sa",
    "gov.sa",
    "net.sa",
    "org.sa",
    "pub.sa",
    "com.sb",
    "gov.sb",
    "net.sb",
    "edu.sb",
    "sc",
    "com.sc",
    "gov.sc",
    "net.sc",
    "org.sc",
    "",
    "edu.sc",
    "sd",
    "com.sd",
    "net.sd",
    "org.sd",
    "edu.sd",
    "med.sd",
    "tv.sd",
    "gov.sd",
    "info.sd",
    "se",
    "org.se",
    "pp.se",
    "tm.se",
    "brand.se",
    "parti.se",
    "press.se",
    "komforb.se",
    "kommunalforbund.se",
    "komvux.se",
    "lanarb.se",
    "lanbib.se",
    "naturbruksgymn.se",
    "sshn.se",
    "fhv.se",
    "fhsk.se",
    "fh.se",
    "mil.se",
    "sg",
    "com.sg",
    "net.sg",
    "org.sg",
    "gov.sg",
    "edu.sg",
    "per.sg",
    "idn.sg",
    "edu.sv",
    "com.sv",
    "gob.sv",
    "org.sv",
    "red.sv",
    "gov.sy",
    "com.sy",
    "net.sy",
    "ac.th",
    "co.th",
    "in.th",
    "go.th",
    "mi.th",
    "or.th",
    "net.th",
    "tj",
    "ac.tj",
    "biz.tj",
    "com.tj",
    "co.tj",
    "edu.tj",
    "int.tj",
    "name.tj",
    "net.tj",
    "org.tj",
    "web.tj",
    "gov.tj",
    "go.tj",
    "mil.tj",
    "com.tn",
    "intl.tn",
    "gov.tn",
    "org.tn",
    "ind.tn",
    "nat.tn",
    "tourism.tn",
    "info.tn",
    "ens.tn",
    "fin.tn",
    "net.tn",
    "to",
    "gov.to",
    "tp",
    "gov.tp",
    "com.tr",
    "info.tr",
    "biz.tr",
    "net.tr",
    "org.tr",
    "web.tr",
    "gen.tr",
    "av.tr",
    "dr.tr",
    "bbs.tr",
    "name.tr",
    "tel.tr",
    "gov.tr",
    "bel.tr",
    "pol.tr",
    "mil.tr",
    "k12.tr",
    "edu.tr",
    "tt",
    "co.tt",
    "com.tt",
    "org.tt",
    "net.tt",
    "biz.tt",
    "info.tt",
    "pro.tt",
    "name.tt",
    "edu.tt",
    "gov.tt",
    "tv",
    "gov.tv",
    "tw",
    "edu.tw",
    "gov.tw",
    "mil.tw",
    "com.tw",
    "net.tw",
    "org.tw",
    "idv.tw",
    "game.tw",
    "ebiz.tw",
    "club.tw",
    "網路.tw",
    "組織.tw",
    "商業.tw",
    "co.tz",
    "ac.tz",
    "go.tz",
    "or.tz",
    "ne.tz",
    "ua",
    "com.ua",
    "gov.ua",
    "net.ua",
    "edu.ua",
    "org.ua",
    "ug",
    "co.ug",
    "ac.ug",
    "sc.ug",
    "go.ug",
    "ne.ug",
    "or.ug",
    "us",
    "ak.us",
    "al.us",
    "ar.us",
    "az.us",
    "ca.us",
    "co.us",
    "ct.us",
    "dc.us",
    "de.us",
    "dni.us",
    "fed.us",
    "fl.us",
    "ga.us",
    "hi.us",
    "ia.us",
    "id.us",
    "il.us",
    "in.us",
    "isa.us",
    "kids.us",
    "ks.us",
    "ky.us",
    "la.us",
    "ma.us",
    "md.us",
    "me.us",
    "mi.us",
    "mn.us",
    "mo.us",
    "ms.us",
    "mt.us",
    "nc.us",
    "nd.us",
    "ne.us",
    "nh.us",
    "nj.us",
    "nm.us",
    "nsn.us",
    "nv.us",
    "ny.us",
    "oh.us",
    "ok.us",
    "or.us",
    "pa.us",
    "ri.us",
    "sc.us",
    "sd.us",
    "tn.us",
    "tx.us",
    "ut.us",
    "vt.us",
    "va.us",
    "wa.us",
    "wi.us",
    "wv.us",
    "wy.us",
    "edu.uy",
    "gub.uy",
    "org.uy",
    "com.uy",
    "net.uy",
    "mil.uy",
    "vatican.va",
    "com.ve",
    "net.ve",
    "org.ve",
    "info.ve",
    "co.ve",
    "web.ve",
    "vi",
    "com.vi",
    "org.vi",
    "edu.vi",
    "gov.vi",
    "vn",
    "com.vn",
    "net.vn",
    "org.vn",
    "edu.vn",
    "gov.vn",
    "int.vn",
    "ac.vn",
    "biz.vn",
    "info.vn",
    "name.vn",
    "pro.vn",
    "health.vn",
    "com.ye",
    "net.ye",
    "ac.yu",
    "co.yu",
    "org.yu",
    "edu.yu",
    "ac.za",
    "city.za",
    "co.za",
    "edu.za",
    "gov.za",
    "law.za",
    "mil.za",
    "nom.za",
    "org.za",
    "school.za",
    "alt.za",
    "net.za",
    "ngo.za",
    "tm.za",
    "web.za",
    "co.zm",
    "org.zm",
    "gov.zm",
    "sch.zm",
    "ac.zm",
    "co.zw",
    "org.zw",
    "gov.zw",
    "ac.zw",
    "co.uk",
    "edu.au",
])
