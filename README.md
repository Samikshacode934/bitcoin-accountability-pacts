#  Bitcoin Accountability Pacts  

**Lock promises on-chain. Break them, burn sats.**  

[![Live Demo](https://img.shields.io/badge/DEMO-bitcoinpacts.carrd.co-orange)](https://bitcoinpacts.carrd.co)  

## How It Works  
1. Users submit promises via Google Form  
2. Manual Bitcoin testnet TX with OP_RETURN  
3. Public burn proof via Blockstream Explorer  

## Future Roadmap  
Future Vision
AI pledge validator: NLP to auto-detect unrealistic/unsafe goals (prototype in progress)

Lightning integration: Micropenalties for small failures (planned next phase)

Mainnet readiness: Designed for covenant-friendly Taproot upgrades



## For Judges  
- [Demo Video][(assets/demo.mp4)](https://youtu.be/_7LOd4dMOU0?si=obf3vdRlciBgpzL3)

- # Documents
- [Project Proposal].[(assets/document)](https://docs.google.com/document/d/1uJhbjUTjKy0dbGgQiF-I1YKaK71hnEm90Jliaa66AKk/edit?tab=t.0
- [Process Documentation](docs/PROCESS.md)


## How It Works (Technical Deep Dive)
```mermaid
graph TD
    A[User Pledge] --> B(OP_RETURN Commitment)
    B --> C{Met Deadline?}
    C -->|Yes| D[Funds Released]
    C -->|No| E[Sats Burned]



## Hackathon Notes
- **Development Time**: 24 hours 
- **Key Innovation**: First behavioral covenant using Bitcoin Script (no ETH/smart contracts)
- **Judges**: See `Future Work` for scalability roadmap

