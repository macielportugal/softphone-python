import pjsua2 as pj
import time

# Subclass to extend the Account and get notifications etc.
class Account(pj.Account):
  def onRegState(self, prm):
      print("***OnRegState: " + prm.reason)

# pjsua2 test function
def pjsua2_test():
  # Create and initialize the library
  ep_cfg = pj.EpConfig()
  ep = pj.Endpoint()
  ep.libCreate()
  ep.libInit(ep_cfg)

  # Create SIP transport. Error handling sample is shown
  sipTpConfig = pj.TransportConfig();
  #sipTpConfig.port = 5061;
  ep.transportCreate(pj.PJSIP_TRANSPORT_UDP, sipTpConfig);
  # Start the library
  ep.libStart();

  acfg = pj.AccountConfig();
  acfg.idUri = "sip:10003@192.168.254.130";
  acfg.regConfig.registrarUri = "sip:192.168.254.130";
  cred = pj.AuthCredInfo("digest", "*", "10003", 0, "123456");
  acfg.sipConfig.authCreds.append( cred );
  # Create the account
  acc = Account();
  acc.create(acfg);
  # Here we don't have anything else to do..
  #time.sleep(10000);

  # Destroy the library
  ep.libDestroy()

#
# main()
#
if __name__ == "__main__":
  pjsua2_test()

