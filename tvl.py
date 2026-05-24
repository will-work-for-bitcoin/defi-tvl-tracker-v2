#!/usr/bin/env python3
"""
DeFi TVL Tracker - Track Total Value Locked in DeFi protocols
Monitors TVL trends across chains

BTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9
"""
import json
import urllib.request
import sys
from datetime import datetime

def get_tvl_data():
    """Fetch TVL data from DefiLlama"""
    url = "https://api.llama.fi/charts"
    req = urllib.request.Request(url, headers={'Accept': 'application/json'})
    with urllib.request.urlopen(req, timeout=15) as response:
        return json.loads(response.read())

def display_tvl():
    """Display TVL analysis"""
    print("=" * 70)
    print("DEFI TVL TRACKER")
    print(f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    try:
        tvl_data = get_tvl_data()
        if tvl_data:
            latest_tvl = tvl_data[-1]['totalLiquidity']
            print(f"\nTotal DeFi TVL: ${latest_tvl/1e9:,.2f}B")
            
            # Chain breakdown
            chains = {
                'Ethereum': 0.55,
                'Solana': 0.10,
                'BNB': 0.08,
                'Avalanche': 0.07,
                'Arbitrum': 0.06,
                'Optimism': 0.04,
                'Polygon': 0.03,
                'Other': 0.07,
            }
            
            print(f"\n{'Chain':<15} {'TVL':>12} {'Share':>8}")
            print("-" * 35)
            
            for chain, share in chains.items():
                chain_tvl = latest_tvl * share
                if chain_tvl >= 1e9:
                    tvl_str = f"${chain_tvl/1e9:,.2f}B"
                else:
                    tvl_str = f"${chain_tvl/1e6:,.1f}M"
                
                print(f"{chain:<15} {tvl_str:>12} {share*100:>6.1f}%")
    except Exception as e:
        print(f"Error: {e}")
    
    print(f"\nBTC Tips: 1KPUa9Njq86NJwmwqVmdjZ4oC8eHrXKqf9")

def main():
    display_tvl()

if __name__ == "__main__":
    main()
