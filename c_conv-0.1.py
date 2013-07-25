import requests
from traits.api import *
from traitsui.api import *

class Currency_Converter(HasTraits):
    convert_from = Str('USD')
    convert_to = Str('GBP')
    value_to_convert = Float(5)
    current_rate = Property(Float, depends_on = 'convert_from, convert_to')
    current_rate_alt = Property(Float, depends_on = 'convert_from, convert_to')
    result = Property(Float, depends_on = 'value_to_convert, current_rate')
    result_alt = Property(Float, depends_on = 'value_to_convert, current_rate_alt')
    
    
    def _get_current_rate(self): 
        convert_from = self.convert_from.upper()
        convert_to = self.convert_to.upper()
        try:
            return requests.get(('http://rate-exchange.appspot.com/currency?from=%s&to=%s&q=1') % (convert_from, convert_to)).json[('v')]        
        except Exception:
            pass
        
        
    def _get_current_rate_alt(self):
        convert_from = self.convert_from.upper()
        convert_to = self.convert_to.upper()
        split1 = (' : 1 %s = ') % convert_from
        strip1 = (' %s</h2>') % convert_to
        try:
            return float(requests.get(('http://themoneyconverter.com/%s/%s.aspx') % (convert_from, convert_to)).text.split(split1)[1].split(strip1)[0].strip())
        except Exception:
            pass
            
    def _get_result(self):
        value_to_convert = self.value_to_convert
        current_rate = self.current_rate
        try:
            return value_to_convert * current_rate
        except Exception:
            pass
        
    def _get_result_alt(self):
        value_to_convert = self.value_to_convert
        current_rate_alt = self.current_rate_alt
        try:
            return value_to_convert * current_rate_alt
        except Exception:
            pass
            
   

Currency_Converter().configure_traits()