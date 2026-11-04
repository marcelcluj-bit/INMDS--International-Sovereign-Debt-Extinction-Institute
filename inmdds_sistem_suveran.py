import time
import random

class SistemINMDSUniversal:
    """
    Sistemul Universal INMDS (Institutul Internațional pentru Stingerea Datoriei Suverane)
    
    Demonstrează tokenizarea datoriei suverane, generarea de surplus condusă de inteligența 
    artificială pe sectoare multiple (Agricultură + Industrie) și protocolul automatizat 
    de răscumpărare și ardere (mecanismul burn) prin contracte inteligente.
    Scalabil pentru mega-economii cu trilioane datorie (ex. SUA, Japonia), gestionând 
    rezervele de token-uri nevândute și piețe multi-nivel (retail tip Forex, bănci, fonduri).
    """
    def __init__(self, cod_stat, datorie_initiala_usd, pib_initial_usd):
        self.cod_stat = cod_stat                      # Identificator generic (ex. "STATUL_SUVERAN_ALPHA")
        self.datorie_totala = datorie_initiala_usd    # Datoria suverană inițială (USD)
        self.pib = pib_initial_usd                    # Produsul Intern Brut inițial (USD)
        self.stoc_tokeni = 0                          # Numărul total de token-uri SBR emise
        self.pret_token = 10.0                        # Valoarea nominală de bază a unui token ($10 USD)
        self.registru_investitori = {}                # Registrul investitorilor pe mai multe niveluri
        self.fond_surplus_productie = 0.0             # Fondul de răscumpărare din surplusul generat de IA (USD)
        
    def raport_stare(self, an):
        tokeni_nealocati = self.stoc_tokeni - sum(self.registru_investitori.values())
        print(f"\n==================================================================")
        print(f"   RAPORT FINANCIAR ANUAL INMDS: ANUL {an} [{self.cod_stat}]")
        print(f"==================================================================")
        print(f" Produsul Intern Brut (PIB):          ${self.pib:,.2f}")
        print(f" Soldul Datoriei Suverane Rămase:     ${self.datorie_totala:,.2f}")
        print(f" Total Token-uri emise (Circulație):  {self.stoc_tokeni:,.0f} SBR")
        print(f" Rezervă Token-uri Nevândute (Tezaur):{max(0, tokeni_nealocati):,.0f} SBR")
        print(f" Fond Acumulat Surplus IA:            ${self.fond_surplus_productie:,.2f}")
        print(f"------------------------------------------------------------------")

    # Etapa 1: Tokenizarea Datoriei la Scară Macro
    def tokenizare_datorie_suverana(self, rată_tokenizata=0.80):
        print(f"\n[INMDS-PROTOCOL] Se execută tokenizarea datoriei suverane ({rată_tokenizata*100:.0f}% alocare)...")
        datorie_convertita = self.datorie_totala * rată_tokenizata
        self.stoc_tokeni = datorie_convertita / self.pret_token
        self.datorie_totala -= datorie_convertita
        print(f"[SUCCES] S-au emis {self.stoc_tokeni:,.0f} token-uri SBR la valoarea nominală de ${self.pret_token:.2f}.")
        print(f"[NOTĂ] Arhitectura scalabilă permite vânzări parțiale; token-urile nevândute rămân în rezerva suverană.")

    # Etapa 2: Achiziția pe Piața Multi-Nivel (Forex, Bănci, Retail, Instituțional)
    def achizitionare_tokeni_piata(self, categorie_cumparator, nume_cumparator, capital_alocat):
        tokeni_alocati = capital_alocat / self.pret_token
        rezervat_curent = sum(self.registru_investitori.values())
        tokeni_disponibili = self.stoc_tokeni - rezervat_curent
        
        if tokeni_alocati <= tokeni_disponibili:
            cheie_intrare = f"[{categorie_cumparator}] {nume_cumparator}"
            self.registru_investitori[cheie_intrare] = self.registru_investitori.get(cheie_intrare, 0) + tokeni_alocati
            print(f"[PIAȚĂ-CUMPĂRARE] {categorie_cumparator} ('{nume_cumparator}') a achiziționat {tokeni_alocati:,.0f} SBR (${capital_allocated:,.2f} USD).")
        else:
            print(f"[AVERTISMENT] Execuție parțială: Capitalul depășește alocarea disponibilă de token-uri pentru '{nume_cumparator}'.")

    # Etapa 3: Optimizare IA Multi-Sectorială (Agricultură + Industrie)
    def ruleaza_ciclu_optimizare_ia(self, an):
        print(f"\n[AI-OPTIMIZATOR] Se implementează optimizarea autonomă pe sectoarele-cheie naționale (Anul {an})...")
        
        # Sectorul 1: Optimizarea randamentului agricol (Agricultură de precizie, gestionarea rețelei de apă/energie IoT)
        rata_crestere_agricola = random.uniform(0.06, 0.10)
        surplus_agricol = self.pib * rata_crestere_agricola
        
        # Sectorul 2: Automatizare industrială și de producție (Eficientizarea lanțului de aprovizionare, conversie energetică fără deșeuri)
        rata_crestere_industriala = random.uniform(0.08, 0.14)
        surplus_industrial = self.pib * rata_crestere_industriala
        
        expansiune_totala_pib = surplus_agricol + surplus_industrial
        self.pib += expansiune_totala_pib
        
        # 40% din surplusul combinat este direcționat direct către Fondul de Răscumpărare a Datoriei
        surplus_capturat = expansiune_totala_pib * 0.40
        self.fond_surplus_productie += surplus_capturat
        
        print(f" -> Creștere Agricultură:   +{rata_crestere_agricola*100:.2f}% (${surplus_agricol:,.2f})")
        print(f" -> Creștere Industrie:      +{rata_crestere_industriala*100:.2f}% (${surplus_industrial:,.2f})")
        print(f" -> Expansiune Totală PIB:   +{(rata_crestere_agricola + rata_crestere_industriala)*100:.2f}% (${expansiune_totala_pib:,.2f})")
        print(f"[ALOCARE FOND] ${surplus_capturat:,.2f} direcționați în Fondul de Răscumpărare Surplus IA.")

    # Etapa 4: Răscumpărare Automatizată prin Contract Inteligent și Arderea Token-urilor (Burn)
    def executa_ardere_contract_inteligent(self):
        print(f"\n[CONTRACT-INTELIGENT] Se execută rutina automatizată de răscumpărare și ardere a token-urilor...")
        if self.fond_surplus_productie > 0 and self.stoc_tokeni > 0:
            fonduri_alocate = self.fond_surplus_productie * 0.80  # 80% din fondul de surplus folosit pentru ardere
            tokeni_de_ars = fonduri_alocate / self.pret_token
            
            if tokeni_de_ars > self.stoc_tokeni:
                tokeni_de_ars = self.stoc_tokeni
                
            valoare_stinsa = tokeni_de_ars * self.pret_token
            self.stoc_tokeni -= tokeni_de_ars
            self.fond_surplus_productie -= valoare_stinsa
            
            print(f"[ARDERE VERIFICATĂ] S-au distrus permanent {tokeni_de_ars:,.0f} token-uri SBR.")
            print(f"[DATORIE REDUSĂ] Valoare Suverană totală stinsă: ${valoare_stinsa:,.2f} USD.")
        else:
            print(f"[INFO] Fondul de răscumpărare este gol sau datoria a fost complet stinsă.")

# --- SIMULARE MEGA-STAT IPOTETIC (Exemplu: 30 Trilioane USD Datorie) ---
if __name__ == "__main__":
    # Modelarea unui stat ipotetic cu economie masivă: 30 Trilioane Datorie, 25 Trilioane PIB
    stat_suveran = SistemINMDSUniversal(
        cod_stat="STATUL_SUVERAN_ALPHA", 
        datorie_initiala_usd=30_000_000_000_000, 
        pib_initial_usd=25_000_000_000_000
    )
    
    stat_suveran.raport_stare(an=0)
    
    # Pasul 1: Tokenizarea a 80% din datoria de 30 Trilioane USD (24 Trilioane USD tokenizate)
    stat_suveran.tokenizare_datorie_suverana(rată_tokenizata=0.80)
    
    # Pasul 2: Participarea pieței globale (Persoane fizice, Bănci, Fonduri, Piață tip Forex)
    stat_suveran.achizitionare_tokeni_piata("PERSOANE_FIZICE_RETAIL", "Public Global / Investitori Retail Forex", 2_000_000_000_000)
    stat_suveran.achizitionare_tokeni_piata("BĂNCI_COMERCIALE", "Consorțiu Interbancar Global", 5_000_000_000_000)
    stat_suveran.achizitionare_tokeni_piata("FONDURI_INSTITUȚIONALE", "Fonduri Suverane & Asigurări", 8_000_000_000_000)
    # Notă: Token-urile rămase nevândute rămân în rezerva de stat (tezaur)
    
    stat_suveran.raport_stare(an=1)
    
    # Pasul 3: Rularea ciclului de 3 ani de optimizare IA (Agricultură + Industrie) cu ardere automată
    for an in range(1, 4):
        stat_suveran.ruleaza_ciclu_optimizare_ia(an=an)
        stat_suveran.executa_ardere_contract_inteligent()
        stat_suveran.raport_stare(an=an)
        time.sleep(0.5)
