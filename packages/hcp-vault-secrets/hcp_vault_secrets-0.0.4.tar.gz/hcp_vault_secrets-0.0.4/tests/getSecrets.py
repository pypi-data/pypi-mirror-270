import sys, os
## Code to disable creating pycache dir after running
sys.dont_write_bytecode = True

sys.path.append(os.path.abspath(f"{os.getcwd()}/src/"))

import hcp_vault_secrets.vaultsecrets as vaultsecrets

hcp = vaultsecrets.vaultsecrets()

prox = hcp.getAppSecret("proxmox", "password")

print(prox)
