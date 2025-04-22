# 📊 Risk to Market (K-NPR) Capital Requirement Calculator

This project provides a full Python-based calculation of **Risk to Market (RtM)** capital requirements for investment firms, in line with the **Investment Firms Regulation (IFR)** and **CRR (EU No 575/2013)**.

It supports three approaches:
- ✅ **Standardised Approach (SA)**  
- 🧮 **Alternative Standardised Approach (ASA)** (FRTB-SA style)  
- 🔬 **Internal Model Approach (IMA)** with Monte Carlo simulation

---

## 🧩 Project Overview

This tool evaluates RtM requirements for:
- **An Equity Call Option** using Black-Scholes model (Delta, Gamma, Vega)
- A full **multi-asset portfolio** including:
  - Equity Futures
  - Government & Corporate Bonds
  - FX Forwards
  - Commodity (Oil) Futures
  - Options (non-linear risk)

---

## ⚙️ Features

- 📘 **Standardised Approach (SA)**:  
  Uses fixed regulatory risk weights per CRR Part Three, Title IV, Chapters 2–4.

- 📘 **Alternative Standardised Approach (ASA)**:  
  Uses stressed FRTB-style sensitivities (60% equity shocks, 25% vol shifts).

- 📘 **Internal Model Approach (IMA)**:  
  Simulates 10-day P&L using normal distributions for each asset class  
  Computes 97.5% **Expected Shortfall (ES)** and multiplies by 1.5 for capital

---

## 🧾 Summary: RtM Methods – Who Uses What and Why

| **Method**                                             | **Who Uses It**                                     | **How It Works**                                                                 | **Why It's Used**                                                                           
|------------------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------|------------------------------------------------------
| 🟩 **Standardised Approach (SA)**                     | **All IFR investment firms**                        | Fixed **risk weights** based on asset class (e.g., 8% for equities)               | ✅ Simple, prescriptive, ensures **minimum capital** without needing complex models      |
| 🟦 **Alternative Standardised (ASA)**<br>*(FRTB-SA)*  | **CRR investment firms** *(large banks, systemic)*   | Based on **sensitivities** (Delta, Vega, Curvature) with **stress-based shocks**  | 🧠 More **risk-sensitive**, but still conservative. Useful for comparability across firms     |
| 🟪 **Internal Model Approach (IMA)**<br>*(FRTB-IMA)* | **Approved CRR banks** *(with regulatory permission)*| Simulates **10-day Expected Shortfall** using historical or Monte Carlo data      | 🎯 Reflects **true risk**, allows for **capital optimisation** if backtesting and models are solid |


---

## 📈 Example Output (IMA):

| Instrument           | Expected Shortfall (97.5%, 10d)| IMA Capital Requirement (×1.5)|
|----------------------|------------------------------- |-------------------------------|
| Equity Call Option   | €59,539.99                     | €89,309.99                    |
| Total Portfolio      | €982,283.43                    | €1,473,425.15                 |


---

## 📎 References

- [Investment Firms Regulation (IFR) – EU 2019/2033](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32019R2033)
- [CRR (EU) No 575/2013 – Title IV, Part Three](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013R0575)
- [FRTB Guidelines – Basel Committee](https://www.bis.org/bcbs/publ/d457.pdf)

---

## 🤝 Contributing

Contributions welcome! Feel free to submit improvements for multi-asset VaR, data ingestion, or visualization enhancements.

---

## 🛡️ Disclaimer

This tool is for **educational and demonstration purposes only**. It is not a substitute for regulatory reporting software or risk engine validation.

---


