# Bitwavie Pricing Service

## Overview

This is the **Pricing Service** for the Bitwavie crypto transaction processing platform. This service provides historical cryptocurrency pricing data for use in transaction analysis and reporting.

## Role in the Bitwavie Platform

The Pricing Service is part of the larger Bitwavie platform, which consists of:

```
/bitwavie/
├── bitwavie_orchestrator_updated/     # Orchestrator Service
├── Bitwavie_universal_fifo_func/      # Universal FIFO Service
├── Bitwavie_per_wallet_fifo_func/     # Per-wallet FIFO Service
├── Bitwavie_pricing_service_func/     # This service (Pricing)
└── README.md
```

## Service Responsibilities

This Pricing Service:

1. Accepts requests for historical cryptocurrency prices
2. Retrieves pricing data from various sources (e.g., Coinbase)
3. Supports multiple time resolutions (e.g., 1d, 1h)
4. Returns accurate pricing data for the specified asset at the given timestamp
5. Provides data in the requested fiat currency (default: USD)

## Integration with Orchestrator

This service is called by the Bitwavie Orchestrator through the `/price` endpoint. The Orchestrator forwards pricing requests with parameters such as asset symbol, timestamp, and optional configuration.

## API Parameters

- `fromSym`: Asset symbol (e.g., BTC, ETH)
- `timestampSEC`: Unix timestamp for the requested price
- `service` (optional): Pricing source (default: coinbase)
- `resolution` (optional): Time resolution (default: 1d)
- `toFiat` (optional): Fiat currency (default: USD)
- `timezone` (optional): Timezone (default: UTC)

## Deployment

This service is deployed to Google Cloud Run at:
https://bitwavie-priceapicaller-455488113475.us-central1.run.app

## Repository

This service is maintained in its own Git repository:
https://github.com/orephillips/Bitwavie-pricingservice.git

## Related Services

- **Orchestrator Service**: Routes requests to this service
- **Universal FIFO Service**: May use this service for pricing data in calculations
- **Per-wallet FIFO Service**: May use this service for pricing data in calculations
