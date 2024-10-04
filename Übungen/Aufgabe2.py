# Funktion zum Eingaben einlesen
def get_valid_int_input(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			print("Bitte eine gültige Zahl eingeben.")

# Einkommen
grundeinkommen = 100_000
abgeordnentenpauschale_frau_p = 50_000
abgeordnentenpauschale_herr_p = 40_000
verdients_je_rede = 500
verdienst_je_stunde_sekeretariat = 200

# Einkommen von Familie P
# Arbeitsumfang einlesen
anz_reden_frau_p = get_valid_int_input("Anzahl der Reden von Frau P: ")
anz_stunden_sekretariat = get_valid_int_input("Anzahl der Stunden Sekretariat Frau P: ")
anz_reden_herr_p = get_valid_int_input("Anzahl der Reden von Herr P: ")
anz_stunden_sekretariat_herr_p = get_valid_int_input("Anzahl der Stunden Sekretariat Herr P: ")

# Einkommen berechen
einkommen_frau_p = grundeinkommen + abgeordnentenpauschale_frau_p + anz_reden_frau_p * verdients_je_rede + anz_stunden_sekretariat * verdienst_je_stunde_sekeretariat
einkommen_herr_p = grundeinkommen + abgeordnentenpauschale_herr_p + anz_reden_herr_p * verdients_je_rede + anz_stunden_sekretariat_herr_p * verdienst_je_stunde_sekeretariat

# Ausgabe
print(f"Gesamteinkommen der Familie P: {einkommen_frau_p + einkommen_herr_p}€")