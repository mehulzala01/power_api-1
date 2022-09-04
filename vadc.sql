SELECT 
    PA_1.PAPMI_No  AS URNo,
    PA_.PAADM_Hospital_DR->HOSP_Desc AS "Episode Service",  
    PA_.PAADM_DepCode_DR->CTLOC_Desc AS "Episode Team",    
    PA_.PAADM_ADMNo AS "Episode No",
    PA_3.Ins_InsType_DR->INST_Desc AS "Episode Payor", 
    PA_3.Ins_AuxInsType_DR->AUXIT_Desc AS "Episode Plan",
    PA_.PAADM_RefDate AS "Referral Date", 
    PA_.PAADM_VisitStatus AS "Episode Status",
    PA_.PAADM_DischgDate AS "Discharge Date",
    PA_2.PAPER_IndigStat_DR->INDST_Desc AS "Indigenous",
    PA_2.PAPER_AgeYr AS "Age in Years" ,
    PA_1.PAPMI_Name2 AS First_Name, 
    PA_1.PAPMI_Name AS "Client_Last_Name", 
    PA_1.PAPMI_DOB AS "DOB", 
    PA_1.PAPMI_Sex_DR->CTSEX_Desc AS "Gender",   
    PA_1.PAPMI_Medicare AS "Medicare_Number", 
    PA_1.PAPMI_MedicareString AS "Medicare_Number_String", 
    PA_1.PAPMI_MedicareCode AS "Medicare_Code", 
    PA_1.PAPMI_MedicareSuffix_DR->MEDSUF_Desc AS "Medicare_Suffix", 
    PA_1.PAPMI_MedicareExpDate AS "Medicare_Expiry_Date", 
    PA_1.PAPMI_PensionType_DR->PENSTYPE_Code AS "Government_Pension_Benefit_Type", 
    CASE 
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '1' THEN 'Age Pension'  
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '2' THEN 'DVA Pension'  
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '3' THEN 'Disability Suppport Pension'  
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '4' THEN 'Carer Payment(Pension)'  
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '5' THEN 'Unemployment-Related Allowance' 
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '6' THEN 'Other Government Pension/Benefit'
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '7' THEN 'No Government Pension/Benefit'  
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '9' THEN 'Not stated adequately'  
        WHEN PA_1.PAPMI_PensionType_DR->PENSTYPE_Code LIKE '' THEN 'Not stated adequately'  
    END     AS "Government_Pension_Benefit_TypeDesc",
    PA_1.PAPMI_GovernCardNo AS "Pension_Number",
    PA_1.PAPMI_ConcessionCardExpDate AS "Pension_Number_Card_Expiry_Date", 
    PA_1.PAPMI_CardType_DR AS "DVA_Card Type",
    CASE 
        WHEN PA_1.PAPMI_CardType_DR LIKE '1' THEN 'Gold Card'  
        WHEN PA_1.PAPMI_CardType_DR LIKE '2' THEN 'White Card'
        WHEN PA_1.PAPMI_CardType_DR LIKE '3' THEN 'DVA entitlement-other'  
        WHEN PA_1.PAPMI_CardType_DR LIKE '4' THEN 'No DVA Entitlement'  
        WHEN PA_1.PAPMI_CardType_DR LIKE '5' THEN 'DVA entitlement-other'  
        WHEN PA_1.PAPMI_CardType_DR LIKE '9' THEN 'Not Stated'  
        WHEN PA_1.PAPMI_CardType_DR LIKE '' THEN 'No DVA Entitlement' 
    END     AS "DVA_Card Type_Desc",
    PA_1.PAPMI_DVAnumber AS "DVA_Card_Number",
    PA_1.PAPMI_CT_Region_DR->CTRG_Desc AS "LGA", 
    PA_1.PAPMI_CountryOfBirth_DR->CTCOU_Desc AS "Country_of_Birth", 
    PA_1.PAPMI_Deceased AS "Deceased", 
    PA_1.PAPMI_CHCPatient AS "Refugee Status", 
    PA_2.PAPER_Name3 AS "Preferred_Name",
    PA_2.PAPER_StName AS "Address_Line",
    {fn concat(upper(PA_2.PAPER_StNameLine1), {fn concat(' ', upper(PA_2.PAPER_ForeignAddress))})}"Address_Line2",
    PA_2.PAPER_CityCode_DR->CTCIT_Desc AS "Suburb", 
    PA_2.PAPER_Zip_DR->CTZIP_Code AS "Postcode",
    PA_2.PAPER_CT_Province_DR->PROV_Desc AS  State, 
    PA_2.PAPER_TelH AS "Home_Phone", 
    PA_2.PAPER_TelO AS "Work_Phone",
    PA_2.PAPER_MobPhone AS "Mobile_Phone",
    PA_2.PAPER_Email AS "Email",
    PA_2.PAPER_PrefLanguage_DR->PREFL_Desc AS "Preferred_Language", 
    PA_2.PAPER_NationalResident AS "Australian_Citizen", 
    PA_2.PAPER_IndigStat_DR->INDST_Desc AS "Indigenous", 
    PA_2.PAPER_InterpreterRequired AS "Communication_Considerations", 
    PA_2.PAPER_PreferredContactMethod AS "Preferred_Contact_Method", 
    PA_2.PAPER_Nation_DR->CTNAT_Desc AS "Cultural_Background",
    PA_2.PAPER_StayingPermanently AS "Chronic_Complex_Care", 
    PA_2.PAPER_Religion_DR->CTRLG_Desc AS "Religion", 
    PA_2.PAPER_TransportUsed_DR AS "HasCarer_code",
    PA_2.PAPER_TransportUsed_DR->TRU_Desc AS "HasCarer",
    PA_2.PAPER_ResidenceStatus_DR->RESID_Desc AS "Residency_Status", 
    PA_2.PAPER_LivingArrangement_DR->LIVARR_Desc AS "Living_Arrangements", 
    PA_2.PAPER_AccomSetting_DR->ACCOMS_Desc AS "Accom_Setting", 
    PA_2.PAPER_DependChildren_DR->DEPCHL_Desc AS "Dependent_Children", 
    PA_2.PAPER_EmploymentStat_DR->EMPLST_Desc AS "Employment_Status", 
    PA_2.PAPER_SourceOfIncome_DR->SRCINC_Desc AS "Healthcare_Card_Status",
    PA_2.PAPER_SocialStatus_DR AS "IsHomeless_Code", 
    PA_2.PAPER_SocialStatus_DR->SS_Desc AS "IsHomeless", 
    PA_2.PAPER_AusSouthSeaIslander_DR->ASSIS_Desc AS "ATSI_Officer_Notification", 
    PA_2.PAPER_DependChildren_DR->DEPCHL_Desc AS "Dependent Children", 
    PA_2.PAPER_InterpreterRequired AS "Interpreter Required", 
    PA_.PAADM_RefStat_DR->RST_Desc AS "Referral_Status", 
    PA_.PAADM_ReferralPriority_DR->REFPRI_Desc AS "Referral_Priority", 
    PA_.PAADM_QualifStatus_DR->QUAL_Desc AS "Legal_Status",
    PA_.PAADM_SourceOfAttend_DR AS "ReferralSource_code", 
    PA_.PAADM_SourceOfAttend_DR->ATTEND_Desc AS "ReferralSource", 
    PA_.PAADM_FamilyDoctor AS "ReferralSource_text",
    PA_.PAADM_NonGovOrg_DR->NGO_Desc AS "Referral Org (External Requestor Details)",
    PA_.PAADM_RefToNGOContactName AS "Carer/Representative_External_Requestor_Details",
    PA_.PAADM_ConsentRecFundInfo AS "ConsentToProvideDetails",
    QAD.ID AS "QAD_ID",
    QAD.QUESPAAdmDR AS "QAD_PAAdmDR",
    QAD.QUESPAPatMasDR AS "QAD_PAPatMasDR",
    QAD.QUESDate AS "QAD_Date_Modified",
    QAD.QUESTime AS "QAD_Time_Modified",
    QAD.QUESStatusDR AS "QAD_Status",
    QAD.QVADCOUTCODE AS "QAD_Outlet_Code",
    QAD.QVADCFIRSTREG AS "QAD_Date_First_Registered",
    QAD.QVADCABI AS "QAD_Aquired_Brain_Injury",
    QAD.QVADCMHDIAG AS "QAD_Mental_Health",
    QAD.QVADCLGB AS "QAD_LGB",
    QAD.QVADCBIRTHSEX AS "QAD_Birth_Sex",
    QAD.QVADCMALTRT AS "QAD_Maltreatment",
    QAD.QVADCMALPERP AS "QAD_Perpetrator",
    QAD.QVADCTARGPOP AS "QAD_Target_Population",
    QAD.QVADCASSESSCOMP AS "QAD_Assessment_Completed",
    QAD.QVADCPRESDRUGOC AS "QAD_Drug",
    QAD.QVADCFORTYP AS "QAD_Forensic",
    QAD.QVADCGENDREAS AS "QAD_Reason_Completed",
    QAD.QVADCSIGGOAL AS "QAD_Significant_Goal",
    QAD.QVADCTIER AS "QAD_Tier",
    QAD.QVADCCRSLEN AS "QAD_Course_Length",
    QAD.QVADCPERCOMP AS "QAD_Percent_Course_Completed",
    QAD.QVADCDELSET AS "QAD_Delivery_Setting",
    QVOUT.ID AS "QOUT_ID",
    QVOUT.QUESPAAdmDR AS "QOUT_PAAdmDR",
    QVOUT.QUESPAPatMasDR AS "QOUT_PAPatMasDR",
    QVOUT.QUESDate AS "QOUT_Date_Modified",
    QVOUT.QUESTime AS "QOUT_Time_Modified",
    QVOUT.QUESStatusDR AS "QOUT_Status",
    QVOUT.QVADCOUTDATE AS "QOUT_Date_Completed",
    QVOUT.QVADCOUTACCOM AS "QOUT_Accomodation",
    QVOUT.QVADCOUTARREST14 AS "QOUT_Arrested",
    QVOUT.QVADCOUTINJDAYS AS "QOUT_Days_Injected",
    QVOUT.QVADCOUTVIOLENT14 AS "QOUT_Violent",
    QVOUT.QVADCOUTPHYSHLTH14 AS "QOUT_Physical_Health",
    QVOUT.QVADCOUTPSYCHHLTH14 AS "QOUT_Psych_Health",
    QVOUT.QVADCOUTQTYLIFE14 AS "QOUT_Quality_Life",
    QVOUT.QVADCOUTEMPL AS "QOUT_Employment",
    QVOUT.QVADCOUTSTUDY AS "QOUT_Study",
    QVOUT.QVADCOUTAUDIT AS "QOUT_AUDIT",
    QVOUT.QVADCOUTDUDIT AS "QOUT_DUDOT",
    QVOUT.QVADCOUTK10 AS "QOUT_KESSLER10",
    QVOUT.QVADCOUTRISKOTH14 AS "QOUT_RiskOthers",
    QVOUT.QVADCOUTRISKSELF14 AS "QOUT_RiskSelf" 
    FROM  questionnaire.QAUXXADVADC QAD  
    RIGHT OUTER JOIN SQLUser.PA_Adm PA_ ON QAD.QUESPAAdmDR=PA_.PAADM_RowID, questionnaire.QAUXXADOUT QVOUT
    RIGHT OUTER JOIN SQLUser.PA_Adm PA_5 ON QVOUT.QUESPAAdmDR=PA_5.PAADM_RowID, SQLUser.PA_AdmInsurance PA_3, SQLUser.PA_PatMas PA_1, 
                    SQLUser.PA_Person PA_2, SQLUser.CT_Hospital CT_ 
    WHERE PA_1.PAPMI_RowId1=PA_.PAADM_PAPMI_DR AND PA_2.PAPER_RowId=PA_1.PAPMI_PAPER_DR AND PA_.PAADM_Hospital_DR=CT_.HOSP_RowId 
        AND PA_3.INS_ParRef=PA_.PAADM_RowID  AND PA_5.PAADM_RowID=PA_.PAADM_RowID 
        AND PA_.PAADM_DepCode_DR->CTLOC_Desc  LIKE 'Maroondah Addictions Recovery Project' 
        AND PA_.PAADM_Hospital_DR->HOSP_Desc LIKE 'Alcohol & Drug'
        AND PA_.PAADM_RefStat_DR IN (1, 4) 
