import os

def installBrave():
	os.system('sudo apt install apt-transport-https curl gnupg')
	os.system('curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -')
	os.system('echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
	os.system('sudo apt update')
	os.system('sudo apt install brave-browser')

installBrave()
