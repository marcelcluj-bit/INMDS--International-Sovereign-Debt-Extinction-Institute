import time
import random

class UniversalINMDSSystem:
    """
    Universal INMDS (International Sovereign Debt Extinction Institute) Engine
    
    Demonstrates sovereign debt tokenization, multi-sector AI-driven surplus generation 
    (Agriculture + Industry), and automated smart-contract redemption (burn mechanism).
    Scalable to mega-economies with trillions in debt (e.g., USA, Japan), accommodating 
    un-purchased token reserves and multi-tier investor markets (Forex-style retail, 
    banks, institutional investment firms).
    """
    def __init__(self, nation_code, initial_debt_usd, initial_gdp_usd):
        self.nation_code = nation_code                # Generic identifier (e.g., "SOVEREIGN_STATE_ALPHA")
        self.total_debt = initial_debt_usd            # Initial Sovereign Debt (USD)
        self.gdp = initial_gdp_usd                    # Initial Gross Domestic Product (USD)
        self.token_supply = 0                         # Total SBR Tokens Issued
        self.token_price = 10.0                       # Base Nominal Token Value ($10 USD)
        self.investor_ledger = {}                     # Multi-tier Investor Ledger
        self.production_surplus_fund = 0.0            # AI Surplus Redemption Pool (USD)
        
    def status_report(self, year):
        unallocated_tokens = self.token_supply - sum(self.investor_ledger.values())
        print(f"\n==================================================================")
        print(f"   INMDS ANNUAL FINANCIAL STATEMENT: YEAR {year} [{self.nation_code}]")
        print(f"==================================================================")
        print(f" Gross Domestic Product (GDP):        ${self.gdp:,.2f}")
        print(f" Remaining Sovereign Debt Balance:    ${self.total_debt:,.2f}")
        print(f" Total Tokens Issued (Circulation):   {self.token_supply:,.0f} SBR")
        print(f" Unsold Token Reserve (Treasury):    {max(0, unallocated_tokens):,.0f} SBR")
        print(f" Accumulated AI Surplus Pool:         ${self.production_surplus_fund:,.2f}")
        print(f"------------------------------------------------------------------")

    # Stage 1: Mega-Scale Debt Tokenization
    def tokenize_sovereign_debt(self, tokenized_ratio=0.80):
        print(f"\n[INMDS-PROTOCOL] Executing Sovereign Debt Tokenization ({tokenized_ratio*100:.0f}% allocation)...")
        debt_converted = self.total_debt * tokenized_ratio
        self.token_supply = debt_converted / self.token_price
        self.total_debt -= debt_converted
        print(f"[SUCCESS] Issued {self.token_supply:,.0f} SBR Tokens at nominal valuation of ${self.token_price:.2f}.")
        print(f"[NOTE] Scalable architecture supports partial sales; unsold tokens remain in sovereign reserve.")

    # Stage 2: Multi-Tier Market Acquisition (Forex / Banks / Retail / Institutional)
    def acquire_tokens_market(self, buyer_category, buyer_name, capital_allocated):
        tokens_allocated = capital_allocated / self.token_price
        current_reserved = sum(self.investor_ledger.values())
        available_tokens = self.token_supply - current_reserved
        
        if tokens_allocated <= available_tokens:
            entry_key = f"[{buyer_category}] {buyer_name}"
            self.investor_ledger[entry_key] = self.investor_ledger.get(entry_key, 0) + tokens_allocated
            print(f"[MARKET-BUY] {buyer_category} ('{buyer_name}') acquired {tokens_allocated:,.0f} SBR (${capital_allocated:,.2f} USD).")
        else:
            print(f"[WARN] Partial execution: Capital exceeds available token allocation for '{buyer_name}'.")

    # Stage 3: Multi-Sector AI Optimization (Agriculture + Industry)
    def execute_ai_optimization_cycle(self, year):
        print(f"\n[AI-OPTIMIZER] Deploying Autonomous Optimization across Key National Sectors (Year {year})...")
        
        # Sector 1: Agricultural Yield Optimization (Precision farming, IoT water/energy grid management)
        agri_growth_rate = random.uniform(0.06, 0.10)
        agri_surplus = self.gdp * agri_growth_rate
        
        # Sector 2: Industrial & Manufacturing Automation (Supply chain streamlining, zero-waste energy conversion)
        industrial_growth_rate = random.uniform(0.08, 0.14)
        industrial_surplus = self.gdp * industrial_growth_rate
        
        total_gdp_expansion = agri_surplus + industrial_surplus
        self.gdp += total_gdp_expansion
        
        # 40% of combined surplus routed directly to the Debt Redemption Pool
        surplus_captured = total_gdp_expansion * 0.40
        self.production_surplus_fund += surplus_captured
        
        print(f" -> Agriculture Growth:  +{agri_growth_rate*100:.2f}% (${agri_surplus:,.2f})")
        print(f" -> Industry Growth:     +{industrial_growth_rate*100:.2f}% (${industrial_surplus:,.2f})")
        print(f" -> Total GDP Expansion: +{(agri_growth_rate + industrial_growth_rate)*100:.2f}% (${total_gdp_expansion:,.2f})")
        print(f"[FUND ALLOCATION] ${surplus_captured:,.2f} routed into AI Surplus Redemption Pool.")

    # Stage 4: Smart Contract Automated Buyback & Token Burn
    def execute_smart_contract_burn(self):
        print(f"\n[SMART-CONTRACT] Executing Automated Token Redemption & Burn Routine...")
        if self.production_surplus_fund > 0 and self.token_supply > 0:
            funds_allocated = self.production_surplus_fund * 0.80  # 80% of surplus pool used for token burn
            tokens_to_burn = funds_allocated / self.token_price
            
            if tokens_to_burn > self.token_supply:
                tokens_to_burn = self.token_supply
                
            extinguished_value = tokens_to_burn * self.token_price
            self.token_supply -= tokens_to_burn
            self.production_surplus_fund -= extinguished_value
            
            print(f"[BURN VERIFIED] Permanently destroyed {tokens_to_burn:,.0f} SBR tokens.")
            print(f"[DEBT REDUCED] Total Sovereign Value Extinguished: ${extinguished_value:,.2f} USD.")
        else:
            print(f"[INFO] Redemption pool empty or debt fully extinguished.")

# --- PRACTICAL SIMULATION ---
if __name__ == "__main__":
    # Hypothetical Mega-State: $30 Trillion Debt, $25 Trillion GDP
    sovereign_state = UniversalINMDSSystem(
        nation_code="SOVEREIGN_STATE_ALPHA", 
        initial_debt_usd=30_000_000_000_000, 
        initial_gdp_usd=25_000_000_000_000
    )
    
    sovereign_state.status_report(year=0)
    
    # Step 1: Tokenize 80% of total debt ($24 Trillion)
    sovereign_state.tokenize_sovereign_debt(tokenized_ratio=0.80)
    
    # Step 2: Multi-tier Global Market Participation
    sovereign_state.acquire_tokens_market("RETAIL_INDIVIDUALS", "Global Public / Retail Forex Investors", 2_000_000_000_000)
    sovereign_state.acquire_tokens_market("COMMERCIAL_BANKS", "Global Interbank Consortium", 5_000_000_000_000)
    sovereign_state.acquire_tokens_market("INSTITUTIONAL_FUNDS", "Sovereign Wealth & Pension Funds", 8_000_000_000_000)
    # Note: Unsold tokens remain in sovereign reserve
    
    sovereign_state.status_report(year=1)
    
    # Step 3: Run 3-Year AI Optimization Cycle (Agriculture + Industry) with Automated Smart Contract Burn
    for year in range(1, 4):
        sovereign_state.execute_ai_optimization_cycle(year=year)
        sovereign_state.execute_smart_contract_burn()
        sovereign_state.status_report(year=year)
        time.sleep(0.5)
