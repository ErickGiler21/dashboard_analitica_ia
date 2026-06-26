import streamlit as st


def apply_styles():
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
html,body,[class*="css"]{font-family:'Inter',sans-serif!important}
.stApp{background:#F4F7FB;color:#0F172A}
.block-container{padding:1.2rem 1.7rem 2rem;max-width:1550px}
#MainMenu,footer,[data-testid="stToolbar"],[data-testid="stDecoration"]{visibility:hidden;height:0}
header{visibility:visible!important;height:2.75rem!important;background:transparent!important}
[data-testid="collapsedControl"]{visibility:visible!important;display:flex!important;opacity:1!important;z-index:999999!important;position:fixed!important;top:84px!important;left:14px!important}
[data-testid="collapsedControl"] button{background:#0F1D3A!important;color:#FFFFFF!important;border:1px solid rgba(255,255,255,.35)!important;border-radius:12px!important;box-shadow:0 10px 24px rgba(15,23,42,.28)!important}
[data-testid="collapsedControl"] svg{color:#FFFFFF!important;stroke:#FFFFFF!important}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#071126,#13295B)!important}
[data-testid="stSidebar"] *{color:#F8FAFC!important}
[data-testid="stFileUploader"] label,[data-testid="stFileUploader"] p,[data-testid="stFileUploader"] small,[data-testid="stFileUploader"] span{color:#334155!important}
[data-testid="stFileUploader"] section{background:#F8FAFC!important;border:1px dashed #94A3B8!important;border-radius:16px!important;padding:14px!important}
[data-testid="stFileUploader"] section:hover{border-color:#2563EB!important;background:#EFF6FF!important}
[data-testid="stFileUploader"] svg{color:#64748B!important;stroke:#64748B!important}
[data-testid="stFileUploader"] button{background:#0F172A!important;color:#FFFFFF!important;border-radius:11px!important;font-weight:850!important;border:0!important}
.brand{display:flex;gap:12px;align-items:center;margin:20px 0 28px}
.brand-icon{width:44px;height:44px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:24px;background:linear-gradient(135deg,#38BDF8,#7C3AED)}
.brand-title{font-size:21px;font-weight:850;color:white}
.brand-sub{font-size:12px;color:#D7E3FF}
.main-title{margin-bottom:18px}
.main-title h1{font-size:31px;letter-spacing:0;margin:0 0 8px;color:#0B1220}
.main-title p{color:#334155;font-size:15px;margin:0}
.metric-card{background:#fff;border:1px solid #CBD5E1;border-radius:16px;padding:16px;min-height:112px;box-shadow:0 8px 22px rgba(15,23,42,.055)}
.metric-label{font-size:11px;text-transform:uppercase;letter-spacing:.05em;font-weight:850;color:#475569}
.metric-value{font-size:29px;line-height:1;font-weight:850;color:#0B1220;margin-top:12px}
.metric-help{font-size:12px;color:#64748B;margin-top:9px}
.metric-icon{float:right;width:42px;height:42px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:22px;background:#E0F2FE}
.metrics-grid{display:grid;grid-template-columns:repeat(4,minmax(145px,1fr));gap:14px;align-items:stretch}
.metrics-grid .metric-card{height:100%;min-height:122px}
.section-title{font-size:17px;font-weight:850;color:#0F172A;margin-bottom:4px}
.section-sub{font-size:13px;color:#64748B;margin-bottom:13px}
.nav-label{font-size:12px;text-transform:uppercase;letter-spacing:.08em;font-weight:850;color:#C7D2FE;margin:0 0 8px}
[data-testid="stSidebar"] [role="radiogroup"]{display:flex;flex-direction:column;gap:9px}
[data-testid="stSidebar"] [role="radio"]{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);border-radius:14px;padding:11px 12px;transition:all .18s ease}
[data-testid="stSidebar"] [role="radio"]:has(input:checked){background:linear-gradient(135deg,rgba(56,189,248,.32),rgba(124,58,237,.38));border-color:rgba(255,255,255,.42);box-shadow:0 10px 22px rgba(0,0,0,.16)}
[data-testid="stSidebar"] [role="radio"] p{font-size:15px;font-weight:850}
.summary-control{background:#fff;border:1px solid #CBD5E1;border-radius:18px;padding:18px;box-shadow:0 8px 22px rgba(15,23,42,.055);margin:0 0 16px}
.summary-control-head{display:flex;gap:13px;align-items:center;margin-bottom:13px}
.summary-control-icon{width:48px;height:48px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:25px;background:linear-gradient(135deg,#38BDF8,#7C3AED);color:#fff}
.summary-control-title{font-size:20px;font-weight:850;color:#0F172A;line-height:1.05}
.summary-control-sub{font-size:13px;color:#64748B;font-weight:700;margin-top:3px}
.control-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.control-item{border:1px solid #D8E2EF;background:#F8FAFC;border-radius:14px;padding:12px}
.control-label{font-size:11px;text-transform:uppercase;letter-spacing:.06em;font-weight:850;color:#64748B;margin-bottom:6px}
.control-value{font-size:15px;font-weight:850;color:#0F172A}
.summary-row{display:grid;grid-template-columns:minmax(280px,.34fr) minmax(0,.66fr);gap:16px;align-items:start;margin-bottom:16px}
.tool-panel{background:#fff;border:1px solid #CBD5E1;border-radius:18px;padding:18px;box-shadow:0 8px 22px rgba(15,23,42,.055)}
.tool-title{font-size:18px;font-weight:850;color:#0F172A;margin-bottom:4px}
.tool-sub{font-size:13px;color:#475569;font-weight:800;margin-bottom:14px}
.summary-section-label{font-size:12px;text-transform:uppercase;letter-spacing:.08em;font-weight:850;color:#475569;margin:18px 0 10px}
.summary-row .summary-section-label{margin-top:0}
.summary-insights{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;margin:10px 0 16px}
.insight-card{background:#fff;border:1px solid #CBD5E1;border-radius:16px;padding:16px;box-shadow:0 8px 22px rgba(15,23,42,.045)}
.insight-title{font-size:13px;text-transform:uppercase;letter-spacing:.06em;font-weight:850;color:#475569;margin-bottom:9px}
.insight-value{font-size:23px;font-weight:850;color:#0B1220;margin-bottom:6px}
.insight-copy{font-size:13px;color:#64748B;line-height:1.45}
.pro-table-wrap{border:1px solid #D8E2EF;border-radius:16px;overflow:auto;background:#fff;max-height:460px;box-shadow:0 6px 18px rgba(15,23,42,.04)}
.pro-table{width:100%;border-collapse:separate;border-spacing:0;font-size:13px;color:#0F172A;background:#fff}
.pro-table th{position:sticky;top:0;z-index:2;background:#EEF4FB;color:#0F172A;text-align:left;font-weight:850;padding:12px 14px;border-bottom:1px solid #CBD5E1;white-space:nowrap}
.pro-table td{padding:11px 14px;border-bottom:1px solid #E2E8F0;color:#0F172A;background:#fff;vertical-align:top}
.pro-table tr:nth-child(even) td{background:#F8FAFC}
.pro-table tr:hover td{background:#EFF6FF}
.tag{display:inline-flex;align-items:center;border-radius:999px;padding:4px 9px;font-weight:850;font-size:12px;white-space:nowrap}
.tag-ok{background:#DCFCE7;color:#047857}
.tag-warn{background:#FEF3C7;color:#B45309}
.tag-bad{background:#FEE2E2;color:#DC2626}
.tag-neutral{background:#E2E8F0;color:#334155}
div[data-testid="stImage"] img{border:1px solid #E2E8F0;border-radius:16px;background:#fff;padding:8px}
.rec{background:#EEF2FF;border:1px solid #C7D2FE;color:#312E81;border-radius:15px;padding:13px 14px;font-weight:800;margin-bottom:10px}
.report-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:14px 0}
.report-card{background:#FFFFFF;border:1px solid #CBD5E1;border-radius:15px;padding:14px;box-shadow:0 8px 20px rgba(15,23,42,.04)}
.report-label{font-size:11px;text-transform:uppercase;letter-spacing:.06em;font-weight:850;color:#64748B;margin-bottom:7px}
.report-value{font-size:22px;font-weight:850;color:#0B1220}
.report-note{background:#ECFDF5;border:1px solid #A7F3D0;color:#065F46;border-radius:16px;padding:15px 16px;font-weight:800;line-height:1.45;margin:12px 0}
.report-panel{background:#FFFFFF;border:1px solid #CBD5E1;border-radius:16px;padding:16px;margin-top:12px;box-shadow:0 8px 20px rgba(15,23,42,.04)}
.report-panel-title{font-size:16px;font-weight:850;color:#0F172A;margin-bottom:10px}
.report-line{display:flex;justify-content:space-between;gap:14px;padding:9px 0;border-bottom:1px solid #E2E8F0;color:#334155}
.report-line:last-child{border-bottom:0}
.report-line b{color:#0F172A}
.stDownloadButton>button{background:linear-gradient(135deg,#2563EB,#7C3AED)!important;color:white!important;border:0!important;border-radius:13px!important;font-weight:850!important}
@media(max-width:1050px){.summary-row,.summary-insights,.report-grid{grid-template-columns:1fr}.control-grid,.metrics-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:720px){.control-grid{grid-template-columns:1fr}.block-container{padding:1rem}}
</style>
        """,
        unsafe_allow_html=True,
    )
