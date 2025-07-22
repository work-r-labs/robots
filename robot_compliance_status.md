# Robot Compliance Status

This document tracks which robot models follow proper conventions and have complete asset files. This serves as a todo list for maintaining and improving robot model compliance.

## Summary Statistics

- **Total Robots**: 63 (44 ABB + 19 Kawasaki)
- **Total URDF files**: 63 
- **Total USD files**: 252 (many robots have multiple USD configurations)
- **With limits.xml**: 30/63 (48%)
- **Forward Kinematics Tests**: 7 test files available
- **Fully Compliant**: 28/63 (44%)
- **Missing limits.xml**: 33 robots
- **Directory Issues**: 2 robots with naming inconsistencies

## Compliance Criteria

For a robot to be considered "fully compliant", it must have:
- ✅ URDF file with correct naming convention
- ✅ USD directory and file structure
- ✅ Meshes directory with STL files
- ✅ limits.xml file for joint limits
- ✅ USD configuration files

## Legend

- ✅ = Present and correct
- ❌ = Missing
- ⚠️ = Present but problematic
- ⚡ = Forward kinematics tests available
- Numbers in parentheses = Count of mesh files

**Test Coverage Types:**
- ✅ All robots: URDF validation tests
- ⚡ Select robots: Forward kinematics (FK) tests

## Robot Status Table

| Robot Model | URDF | USD | Meshes | Limits | Config | Tests | Status | Priority |
|-------------|------|-----|--------|--------|--------|-------|---------|----------|
| CRB15000_10kg_152_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ⚡+✅ | **COMPLIANT** | ✅ |
| CRB15000_12kg_127_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ⚡+✅ | **COMPLIANT** | ✅ |
| CRB15000_5kg_950_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ⚡+✅ | **COMPLIANT** | ✅ |
| IRB1010_1_5kg_370_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB1100_4kg_475_STD_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ⚡+✅ | **COMPLIANT** | ✅ |
| IRB1100_4kg_580_STD_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB1200_5_90_STD_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ⚡+✅ | **COMPLIANT** | ✅ |
| IRB1200H_5_90_STD_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ⚡+✅ | **COMPLIANT** | ✅ |
| IRB1200H_7_70_STD_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB14000_Yumi_v1 | ✅ | ✅ | ✅ (15) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| IRB14050_SAYuMi_v1 | ✅ | ✅ | ✅ (8) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| IRB1520ID_4_150_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB1600_X-120_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB52_7-1_2-Short_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB52_7-1_45-Long_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB5500-22_v1 | ✅ | ✅ | ✅ (8) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB5500-27_v1 | ✅ | ✅ | ✅ (9) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB5510-12_v1 | ✅ | ✅ | ✅ (8) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB6750S_185-390-LID_v1 | ✅ | ✅ | ✅ (8) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB8700_550-420-SW6_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB8700_800_350_v1 | ✅ | ✅ | ✅ (8) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB910INV-350_v1 | ✅ | ✅ | ✅ (4) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB910INV-550_v1 | ✅ | ✅ | ✅ (5) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB920T_6kg_450_180_STD_v1 | ✅ | ✅ | ✅ (4) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB920_6kg_550-180-STD_v1 | ✅ | ✅ | ✅ (4) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB920_6kg_650_180_STD_v1 | ✅ | ✅ | ✅ (4) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| IRB930_12kg_1050_300_STD_v1 | ✅ | ✅ | ✅ (4) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| Irbpa_250_D1000_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (3) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpa_500_D1000_H700_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (3) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpa_500_D1450_H900_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (3) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpa_750_D1000_H700_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (4) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpb_250_D1000_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (6) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpb_500_D1450_v1 | ✅ | ✅ | ✅ (6) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpb_750_D1450_v1 | ✅ | ✅ | ✅ (6) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpc_1000_v1 | ✅ | ✅ | ✅ (2) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpc_500_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (2) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpd_600_D1000_L1600_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (6) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpd_600_D1200_L2000_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (6) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpk_1000_D1400_L4000_v1 | ✅ | ✅ | ✅ (4) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpk_600_D1200_L1600_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (4) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpl_1000_L1250_v1 | ✅ | ✅ | ✅ (2) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpl_5000_v1 | ✅ | ✅ | ✅ (2) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpr_1000_D1200_L2000_IRC5_rev02_CAD_v1 | ✅ | ✅ | ✅ (4) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| Irbpr_300_D1000_L1250_v1 | ✅ | ✅ | ✅ (4) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| BT200L_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | Name mismatch | 🟡 |
| BX100N_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| BX100S_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| BX130X_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | **COMPLIANT** | ✅ |
| BX200L_v1 | ✅ | ✅ | ✅ (7) | ✅ | ✅ | ✅ | Name mismatch | 🟡 |
| CL103_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS003N_A001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS005L_A001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS005N_A001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS006L_A001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS007L_BC01_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS007N_BC01_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS013N_AC01_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS015X_B001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS020N_A001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS025N_AC01_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS030N_B001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS050N_B001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |
| RS080N_B001_v1 | ✅ | ✅ | ✅ (7) | ❌ | ✅ | ✅ | Missing limits | 🔴 |

## Priority Tasks

### 🔴 High Priority (Critical Issues)

**Missing limits.xml files (33 robots):**
- IRB14000_Yumi_v1, IRB14050_SAYuMi_v1 (dual-arm robots)
- All ABB positioner robots (Irbpa*, Irbpb*, Irbpc*, Irbpd*, Irbpk*, Irbpl*, Irbpr*) - 16 robots
- All Kawasaki RS series robots (15 robots): RS003N_A001_v1, RS005L_A001_v1, RS005N_A001_v1, RS006L_A001_v1, RS007L_BC01_v1, RS007N_BC01_v1, RS013N_AC01_v1, RS015X_B001_v1, RS020N_A001_v1, RS025N_AC01_v1, RS030N_B001_v1, RS050N_B001_v1, RS080N_B001_v1
- CL103_v1 (Kawasaki)

### 🟡 Medium Priority (Naming Issues)

Fix naming mismatches for 2 robots:
- BT200L_v1 (directory vs URDF name mismatch)
- BX200L_v1 (directory vs URDF name mismatch)  

### ✅ Low Priority (Compliant Robots)

28 robots are fully compliant and require no immediate action.

## Next Steps

1. **Create limits.xml files** for 33 robots missing joint limits (highest priority)
2. **Fix naming inconsistencies** for 2 robots with directory/file mismatches
3. **Expand FK test coverage** beyond current 7 robots
4. **Add missing thumbnails** for robots that lack them
5. **Improve USD configuration** consistency across all robots

## Validation Commands

```bash
# Check all URDF files
bash tools/validate_all_urdfs.sh

# Check specific robot
uv run tools/validate_urdf.py library/ABB/RobotName_v1/RobotName.urdf
```

---
*Last updated: 2025-07-22 by /update-compliance-table command*
*Total robots scanned: 63 (44 ABB + 19 Kawasaki)*
*Compliance rate: 44% (28/63 fully compliant)*
*Generated by Claude Code*