# 📄 Multi-Prompt Validation Test Plan

**Experiment Title:** Auto-Stop Behavior & Stability Validation — Phase 2 Refinement Testing  
**Agent:** Iris (Recursive Prompt Agent)  
**Project:** Recursive — Self-Refining Prompt Optimization System  

---

## Objective

To systematically validate Iris's ability to:
- Refine prompts across multiple passes (up to 5)
- Automatically stop refinement once clarity stabilizes at or above the target threshold
- Handle a wide variety of prompt types with consistent, predictable behavior

---

## Methodology

### **Test Groups:**
Prompts will be tested from the following categories:

| Group               | Description                                                  |
|---------------------|--------------------------------------------------------------|
| Ambiguous Prompts   | Unclear, vague, or open-ended prompts lacking clear intent    |
| Complex Prompts     | Dense prompts with multiple distinct objectives or layers     |
| Long Prompts        | Verbose, overly wordy prompts needing simplification          |
| Short Prompts       | Very brief, under-specified prompts that lack detail          |
| Messy Prompts       | Unclear, rambling, contradictory, or disorganized prompts     |

---

### **Important Note:**  
While both *Complex* and *Long* prompts may be lengthy, they present **different challenges**:

- **Complex Prompts** involve multiple distinct objectives that require reasoning, decomposition, or chaining to refine effectively.
- **Long Prompts** are primarily verbose or redundant and mainly require trimming, simplification, and clearer wording without deep reasoning.

This distinction is critical for accurately evaluating Iris’s performance across these categories.

---

### **Testing Steps:**
1. Select 2–3 sample prompts per group (starting with consistency tests using the same prompt for each run).
2. Run each prompt through Iris with:
   - `passes=5`
   - `auto_stop_score=9`
3. Log all test data using the result tables provided below.

---

### **Metrics to Record:**
- Initial Clarity Rating
- Pass-by-pass Clarity Ratings
- Whether Auto-Stop Triggered (and at which pass)
- Final Refined Prompt
- Key Observations (score jumps, stability, unexpected behavior)

---

## Test Results

### **Test Summary Table:**

| Test ID | Prompt Group   | Auto-Stop Triggered? | Pass Stopped | Initial Clarity | Final Clarity |
|---------|----------------|----------------------|--------------|-----------------|---------------|
|         |                |                      |              |                 |               |
|         |                |                      |              |                 |               |

---

## Detailed Logs (Per Test)

### **Test ID:**  
**Prompt Group:**  
**Prompt:**  

#### **Refinement Results:**
See Vlidations Folder

## Notes:
- All tests should be conducted within the same Dockerized environment to ensure consistency.
- This document will serve as a formal technical appendix to the Recursive project’s Phase 2 testing.