import json
import re
from bs4 import BeautifulSoup

def clean_for_filename(value):
    cleaned_value = re.sub(r'[^\w\s.-]', '', value)
    return cleaned_value

def output_combinations(combinations):
    cleaned_combinations = []
    for combination in combinations:
        cleaned_combination = {key: clean_for_filename(value) for key, value in combination.items()}
        cleaned_combinations.append(cleaned_combination)
    return cleaned_combinations

html = """ 
<!DOCTYPE html>
<html>
<head>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="format-detection" content="telephone=no">
<link rel="stylesheet" type="text/css" href="/bmw/style.css">
<script>
  window.googletag = window.googletag || { cmd: [] };
  googletag.cmd.push(function () {
    googletag.pubads().set("page_url", "https://www.realoem.com/");
  });
</script>
<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-1518611-1']);
_gaq.push(['_trackPageview']);
(function() {
 var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
 ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
 var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
})();
</script>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-MPR6S5D07L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-MPR6S5D07L');
</script>
<script type="text/javascript">
_atrk_opts = { atrk_acct:"ypyPf1agwt00i0", domain:"realoem.com",dynamic: true};
(function() { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://certify-js.alexametrics.com/atrk.js"; var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as, s); })();
</script>
<script async src="https://cdn.fuseplatform.net/publift/tags/2/2649/fuse.js"></script>
<noscript><img src="https://certify.alexametrics.com/atrk.gif?account=ypyPf1agwt00i0" style="display:none" height="1" width="1" alt="image" /></noscript>
<script type="text/javascript" src="/bmw/js/m.js"></script>
	<script type="text/javascript" src="/bmw/js/main.js"></script>
	<title>RealOEM.com - Select Your BMW Model</title>
	<meta name="description" content="RealOEM.com BMW Parts website. This site can be used to look up BMW part numbers and approximate part prices. The Parts are grouped into diagrams and diagrams are grouped into categories and subcategories">
	<meta name="keywords" content="bmw parts,bmw parts catalog,bmw epc">
	<meta name="robots" content="noodp,noydir">
</head>
<body>
<div class="grid">
		<div id="rightnav">
			<div class="lang">
			<a href="//www.nemigaparts.com/cat_spares/">Other Brands</a>
				Language: <select id="lsel" name="langDefault"><option value="cs">český</option><option value="de">deutsch</option><option value="el">ελληνικά</option><option value="en">english</option><option value="enUS" selected="selected">US english</option><option value="es">español</option><option value="fr">Français</option><option value="it">italiano</option><option value="ja">日本語</option><option value="ko">한국어</option><option value="nl">Nederlands</option><option value="pl">polski</option><option value="pt">português</option><option value="ru">русский</option><option value="sv">svensk</option><option value="th">ภาษาไทย</option><option value="tr">Türkçe</option><option value="zh">汉语</option><option value="zhTW">繁體中文</option></select></div>
		</div>
		<div id="main">
			<h2>RealOEM.com: Select Your BMW Model</h2>

			<div class="splinks">
</div>
<div class="splinks iad-mt">
<div id="ezoic-pub-ad-placeholder-623">
<a href="http://www.bmwmobiletradition-online.com" target="_blank"><img src="/bmw/assets/bmw-mobile-trad-728x90.gif" width="728" height="90" alt="BMW Mobile Tradition"></a>
<br>
</div>
<a href="mailto:support@realoem.com">banner ads by realoem</a>
</div>
<div class="tbl">
			<div class="blk">
			<div class="column">
				Enter your BMW Serial Number (<b>last 7 digits of your VIN</b>) <b>OR</b> use the search options below.<div class="searchForm">
					<form name="form2" action="/bmw/enUS/select">
						<label for="vin">Serial Number:</label>
						<input id="vin" name="vin" type="text" value="" size="10" maxlength="7"/><input type="submit" value="Search" />
						<span class="rpad2">
							Catalog: 12/2019</span>
					</form>
				</div>
			</div>
			<div>
				<div class="searchForm">
					<form name="form3" action="/bmw/enUS/partxref">
						<label for="q">PART NR APPLICATION SEARCH:</label>
						<input name="q" size="10" maxlength="20" />
						<input type="submit" value="Search" />
					</form>
				</div>
			</div>

			<div id="selectForm">
				<form name="form1" action="/bmw/enUS/select">

					<div class="selcolumn">
						<label for="product">Product:</label>
						<select id="product" name="product" onchange="postback(1,this)" size="3"><option value="P" selected="selected">Car</option><option value="M">Motorcycle</option></select><label for="archive">Catalog:</label>
						<select id="archive" name="archive" onchange="postback(1,this)" size="3"><option value="0">Current</option><option value="1" selected="selected">Classic</option></select></div>

					<div class="selcolumn">
							<label for="series">Series:</label>
							<select id="series" name="series" onchange="postback(2,this)" size="15"><option value="ISE">Isetta&emsp;(1955 &mdash; 1962)</option><option value="700" selected="selected">700&emsp;(1959 &mdash; 1965)</option><option value="114">1502-2002tii&emsp;(1966 &mdash; 1977)</option><option value="E21">3' E21&emsp;(1975 &mdash; 1983)</option><option value="E30">3' E30&emsp;(1981 &mdash; 1994)</option><option value="E36">3' E36&emsp;(1989 &mdash; 2000)</option><option value="NK">1500-2000CS&emsp;(1962 &mdash; 1972)</option><option value="E12">5' E12&emsp;(1972 &mdash; 1981)</option><option value="E28">5' E28&emsp;(1980 &mdash; 1990)</option><option value="E34">5' E34&emsp;(1987 &mdash; 1996)</option><option value="E39">5' E39&emsp;(1995 &mdash; 2003)</option><option value="E9">2.5CS-3.0CSL&emsp;(1968 &mdash; 1975)</option><option value="E24">6' E24&emsp;(1975 &mdash; 1989)</option><option value="V8">V8&emsp;(1952 &mdash; 1965)</option><option value="E3">2500-3.3Li&emsp;(1968 &mdash; 1977)</option><option value="E23">7' E23&emsp;(1976 &mdash; 1989)</option><option value="E32">7' E32&emsp;(1985 &mdash; 1994)</option><option value="E38">7' E38&emsp;(1993 &mdash; 2001)</option><option value="E31">8' E31&emsp;(1989 &mdash; 1999)</option><option value="E26">M1 E26&emsp;(1980 &mdash; 1981)</option><option value="Z1">Z1 Roadster&emsp;(1988 &mdash; 1991)</option><option value="Z3">Z3 E36&emsp;(1994 &mdash; 2002)</option><option value="E52">Z8 E52&emsp;(1998 &mdash; 2003)</option><option value="VET">Veteranen&emsp;(1933 &mdash; 1941)</option><option value="CMSP">BMW Classic Motorsport&emsp;(1928 &mdash; 1937)</option></select></div>
						<div class="selcolumn">
							<label for="body">Body:</label>
							<select id="body" name="body" onchange="postback(3,this)" size="15"><option value="Cab" selected="selected">Convertible</option><option value="Cou">Coupe</option><option value="Lim">Sedan</option></select></div>
					<div class="selcolumn">
							<label for="model">Model:</label>
							<select id="model" name="model" onchange="postback(4,this)" size="15"><option value="700" selected="selected">700</option></select></div>
					<div class="selcolumn">
							<label for="market">Market:</label>
							<select id="market" name="market" onchange="postback(5,this)" size="15"><option value="EUR" selected="selected">EUR</option></select></div>
					<div class="selcolumn">
							<label for="prod">Prod Month:</label>
							<select id="prod" name="prod" onchange="postback(6,this)" size="15"><optgroup label="1961">
										<option value="19610100">01/1961</option><option value="19610200">02/1961</option><option value="19610300">03/1961</option><option value="19610400">04/1961</option><option value="19610500">05/1961</option><option value="19610600">06/1961</option><option value="19610700">07/1961</option><option value="19610800">08/1961</option><option value="19610900">09/1961</option><option value="19611000">10/1961</option><option value="19611100">11/1961</option><option value="19611200">12/1961</option></optgroup>
								<optgroup label="1962">
										<option value="19620100">01/1962</option><option value="19620200">02/1962</option><option value="19620300">03/1962</option><option value="19620400">04/1962</option><option value="19620500">05/1962</option><option value="19620600">06/1962</option><option value="19620700">07/1962</option><option value="19620800">08/1962</option><option value="19620900">09/1962</option><option value="19621000">10/1962</option><option value="19621100">11/1962</option><option value="19621200">12/1962</option></optgroup>
								<optgroup label="1963">
										<option value="19630100">01/1963</option><option value="19630200">02/1963</option><option value="19630300">03/1963</option><option value="19630400">04/1963</option><option value="19630500">05/1963</option><option value="19630600">06/1963</option><option value="19630700">07/1963</option><option value="19630800">08/1963</option><option value="19630900">09/1963</option><option value="19631000">10/1963</option><option value="19631100">11/1963</option><option value="19631200">12/1963</option></optgroup>
								<optgroup label="1964">
										<option value="19640100">01/1964</option><option value="19640200">02/1964</option><option value="19640300">03/1964</option><option value="19640400">04/1964</option><option value="19640500">05/1964</option><option value="19640600">06/1964</option><option value="19640700">07/1964</option><option value="19640800">08/1964</option><option value="19640900">09/1964</option></optgroup>
								</select></div>
					<div class="selcolumn">
						</div>

					<div class="gad-select-square">
<div class="splinks">
</div>
</div>
</form>
			</div>

			<a id="visible"></a>
			
			<div class="splinks vs2">
</div>
<p class="copy">
</div>
			<div class="blk gad-tall-right">
<div class="sticky">
<div class="splinks">
</div>
</div>
</div></div>
		</div>
	</div>
<script type="text/javascript">
var _qevents = _qevents || [];
(function() {
var elem = document.createElement('script');
elem.src = (document.location.protocol == "https:" ? "https://secure" : "http://edge") + ".quantserve.com/quant.js";
elem.async = true;
elem.type = "text/javascript";
var scpt = document.getElementsByTagName('script')[0];
scpt.parentNode.insertBefore(elem, scpt);
})();
_qevents.push({
qacct:"p-h8wAabTPpGCtz"
});
</script>
<noscript>
<div style="display:none;">
<img src="//pixel.quantserve.com/pixel/p-h8wAabTPpGCtz.gif" border="0" height="1" width="1" alt="Quantcast"/>
</div>
</noscript>
<!-- Start Alexa Certify Javascript -->
<script type="text/javascript">
_atrk_opts = { atrk_acct:"ypyPf1agwt00i0", domain:"realoem.com",dynamic: true};
(function() { var as = document.createElement('script'); as.type = 'text/javascript'; as.async = true; as.src = "https://d31qbv1cthcecs.cloudfront.net/atrk.js"; var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(as, s); })();
</script>
<noscript><img src="https://d5nxst8fruw4z.cloudfront.net/atrk.gif?account=ypyPf1agwt00i0" style="display:none" height="1" width="1" alt="" /></noscript>
<!-- End Alexa Certify Javascript -->
<script>
  var _comscore = _comscore || [];
  _comscore.push({ c1: "2", c2: "14576572" });
  (function() {
    var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;
    s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
    el.parentNode.insertBefore(s, el);
  })();
</script>
<noscript>
  <img src="https://b.scorecardresearch.com/p?c1=2&c2=14576572&cv=2.0&cj=1" alt="image" />
</noscript>
</body>
</html>
 """

soup = BeautifulSoup(html, 'html.parser')

# Extract BMW Car Data
car_data = {}

# Extract Series, Body Types, Models, Markets, Production Months
series_select = soup.find('select', {'id': 'series'})
body_select = soup.find('select', {'id': 'body'})
model_select = soup.find('select', {'id': 'model'})
market_select = soup.find('select', {'id': 'market'})
prod_select = soup.find('select', {'id': 'prod'})

# Check if elements exist before extracting data
series_options = [option.text.strip() for option in series_select.find_all('option')] if series_select else []
body_options = [option.text.strip() for option in body_select.find_all('option')] if body_select else []
model_options = [option.text.strip() for option in model_select.find_all('option')] if model_select else []
market_options = [option.text.strip() for option in market_select.find_all('option')] if market_select else []
prod_options = [option.text.strip() for option in prod_select.find_all('option')] if prod_select else []

# Create combinations
combinations = []
for series in series_options:
    for body in body_options:
        for model in model_options:
            for market in market_options:
                for prod in prod_options:
                    combinations.append({
                        'Series': series,
                        'Body': body,
                        'Model': model,
                        'Market': market,
                        'Production_Month': prod
                    })

# Output cleaned combinations to a single file
cleaned_combinations = output_combinations(combinations)

# Write the cleaned combinations to a JSON file
output_file = 'bmw_combinations.json'
with open(output_file, 'w') as json_file:
    json.dump(cleaned_combinations, json_file, indent=2)

# Count the number of combinations
num_combinations = len(cleaned_combinations)
print(f"Combinations have been saved to {output_file}")
print(f"Number of combinations: {num_combinations}")

