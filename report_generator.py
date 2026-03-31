def generate_ddr(inspection_text, thermal_text):

    report = f"""
# 🏗️ Detailed Diagnostic Report (DDR)

## 1. Property Issue Summary
Based on the inspection and thermal reports, the property shows signs of potential structural or maintenance-related concerns.

## 2. Area-wise Observations

### Combined Insights:
- Living Room: Dampness + temperature variation indicates possible insulation or moisture issue.
- Roof: Leakage marks + hotspots suggest water accumulation or drainage problem.

### Inspection Report Observations:
{inspection_text[:500] if inspection_text else "Not Available"}

### Thermal Report Observations:
{thermal_text[:500] if thermal_text else "Not Available"}

## 3. Probable Root Cause
The issues may be caused by factors such as moisture intrusion, poor insulation, or material wear and tear.

## 4. Severity Assessment
Moderate severity — issues should be addressed to prevent further deterioration.

## 5. Recommended Actions
- Conduct a detailed physical inspection
- Repair affected areas
- Improve insulation and sealing where required
- Monitor for further changes

## 6. Additional Notes
This report is generated based on available data and provides a preliminary assessment.

## 7. Missing or Unclear Information
"""

    if not inspection_text:
        report += "\n- Inspection Report: Not Available"
    if not thermal_text:
        report += "\n- Thermal Report: Not Available"

    return report