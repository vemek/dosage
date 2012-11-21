# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile, IGNORECASE
from ..scraper import _BasicScraper
from ..helpers import indirectStarter
from ..util import tagre


class TalesOfPylea(_BasicScraper):
    latestUrl = 'http://talesofpylea.com/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(r'<img src="(istrip_files/strips/.+?)"')
    prevSearch = compile(r' <a href="(.+?)">Back</a>')
    help = 'Index format: nnn'



class TheNoob(_BasicScraper):
    latestUrl = 'http://www.thenoobcomic.com/index.php'
    stripUrl = latestUrl + '?pos=%'
    imageSearch = compile(r'<img src="(/headquarters/comics/.+?)"')
    prevSearch = compile(r'<a class="comic_nav_previous_button" href="(.+?)"></a>')
    help = 'Index format: nnnn'



class TheOrderOfTheStick(_BasicScraper):
    latestUrl = 'http://www.giantitp.com/'
    stripUrl = latestUrl + 'comics/images/%s'
    imageSearch = compile(r'<IMG src="(/comics/images/.+?)">')
    prevSearch = compile(r'<A href="(/comics/oots\d{4}\.html)"><IMG src="/Images/redesign/ComicNav_Back.gif"')
    help = 'Index format: n (unpadded)'
    starter = indirectStarter('http://www.giantitp.com/', compile(r'<A href="(/comics/oots\d{4}\.html)"'))



class TheParkingLotIsFull(_BasicScraper):
    latestUrl = 'http://plif.courageunfettered.com/archive/arch2002.htm'
    stripUrl = 'http://plif.courageunfettered.com/archive/wc%s.gif'
    imageSearch = compile(r'<td align="center"><A TARGET=_parent HREF="(wc\d+\..+?)">')
    prevSearch = compile(r'-\s*\n\s*<A HREF="(arch\d{4}\.htm)">\d{4}</A>')
    help = 'Index format: nnn'



class TheWotch(_BasicScraper):
    latestUrl = 'http://www.thewotch.com/'
    stripUrl = latestUrl + '?epDate=%s'
    imageSearch = compile(r"<img.+?src='(comics/.+?)'")
    prevSearch = compile(r"<link rel='Previous' href='(\?epDate=\d+-\d+-\d+)'")
    help = 'Index format: yyyy-mm-dd'


class Thorn(_BasicScraper):
    latestUrl = 'http://www.mimisgrotto.com/thorn/index.html'
    stripUrl = 'http://www.mimisgrotto.com/thorn/%s.html'
    imageSearch = compile(r'"(strips/.+?)"')
    prevSearch = compile(r'(\d[\d][\d].html)">Prev')
    help = 'Index format: nnn'


class TinyKittenTeeth(_BasicScraper):
    latestUrl = 'http://www.tinykittenteeth.com/'
    stripUrl = latestUrl + 'index.php?current=%s'
    imageSearch = compile(tagre("img", "src", r'(http://www\.tinykittenteeth\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)', after="Previous"))
    help = 'Index format: n (unpadded)'


class TwoTwoOneFour(_BasicScraper):
    latestUrl = 'http://www.nitrocosm.com/go/2214_classic/'
    stripUrl = latestUrl + '%s/'
    imageSearch = compile(r'<img class="gallery_display" src="([^"]+)"')
    prevSearch = compile(r'<a href="([^"]+)"[^>]*><button type="submit" class="nav_btn_previous">')
    help = 'Index format: n (unpadded)'



class TheWhiteboard(_BasicScraper):
    latestUrl = 'http://www.the-whiteboard.com/'
    stripUrl = latestUrl + 'auto%s.html'
    imageSearch = compile(r'<img SRC="(autotwb\d{1,4}.+?|autowb\d{1,4}.+?)">', IGNORECASE)
    prevSearch = compile(r'&nbsp<a href="(.+?)">previous</a>', IGNORECASE)
    help = 'Index format: twb or wb + n wg. twb1000'



class HMHigh(_BasicScraper):
    name = 'TheFallenAngel/HMHigh'
    latestUrl = 'http://www.thefallenangel.co.uk/hmhigh/'
    stripUrl = latestUrl + '?id=%s'
    imageSearch = compile(r'<img src="(http://www.thefallenangel.co.uk/hmhigh/img/comic/.+?)"')
    prevSearch = compile(r' <a href="(http://www.thefallenangel.co.uk/.+?)" title=".+?">Prev</a>')
    help = 'Index format: nnn'



class TheOuterQuarter(_BasicScraper):
    latestUrl = 'http://theouterquarter.com/'
    stripUrl = latestUrl + 'comic/%s'
    imageSearch = compile(r'<img src="(http://theouterquarter.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="([^"]+)" rel="prev">')
    help = 'Index format: nnn'



class TheHorrificAdventuresOfFranky(_BasicScraper):
    latestUrl = 'http://www.boneyardfranky.com/'
    stripUrl = latestUrl + '?p=%s'
    imageSearch = compile(r'<img src="(http://www.boneyardfranky.com/comics/.+?)"')
    prevSearch = compile(r'<div class="nav-previous"><a href="(.+?)">')
    help = 'Index format: nnn'
