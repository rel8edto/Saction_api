import requests
from lxml import html

# https://sanctionssearch.ofac.treas.gov/






def searchOfac(keyword,count=5):
    cookies = {
        '_gid': 'GA1.2.679650639.1674763855',
        '_ga': 'GA1.1.888145252.1674763855',
        'nmstat': '1a332339-7087-27db-4c86-548d36f20041',
        '_ga_008DHEJFE8': 'GS1.1.1674763855.1.1.1674763876.0.0.0',
        'ASP.NET_SessionId': 'wlrojwfjh3coh1saq25uypoe',
        'BIGipServerEzM5bUtMV5dP4OkrzH904A': '!b+N2ABhLDHeGBu9Ica4I6euaNKjHzqkUsm5Tbvcn2pfWaz4JMPPO++VcKascTVv4BXstypmz43HvSzA=',
        'TS01681a3a': '01f6e3b1e9bddcc5788b40e36286a58232247366664dc37f7483fa62727eb0b64ef0d75e5516ceb2589289bc077f2452092022226f3c4fcca500838ae58503edd42173f7359c9cb43ae5880d51658b994df3bb5fb9',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-CA,en;q=0.9,zh-CA;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 'Cookie': '_gid=GA1.2.679650639.1674763855; _ga=GA1.1.888145252.1674763855; nmstat=1a332339-7087-27db-4c86-548d36f20041; _ga_008DHEJFE8=GS1.1.1674763855.1.1.1674763876.0.0.0; ASP.NET_SessionId=wlrojwfjh3coh1saq25uypoe; BIGipServerEzM5bUtMV5dP4OkrzH904A=!b+N2ABhLDHeGBu9Ica4I6euaNKjHzqkUsm5Tbvcn2pfWaz4JMPPO++VcKascTVv4BXstypmz43HvSzA=; TS01681a3a=01f6e3b1e9bddcc5788b40e36286a58232247366664dc37f7483fa62727eb0b64ef0d75e5516ceb2589289bc077f2452092022226f3c4fcca500838ae58503edd42173f7359c9cb43ae5880d51658b994df3bb5fb9',
        'Origin': 'https://sanctionssearch.ofac.treas.gov',
        'Pragma': 'no-cache',
        'Referer': 'https://sanctionssearch.ofac.treas.gov/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'dnt': '1',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'ctl00_ctl03_HiddenField': ';;AjaxControlToolkit, Version=3.5.40412.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:1547e793-5b7e-48fe-8490-03a375b13a33:475a4ef5:5546a2b:d2e10b12:497ef277:effe2a26',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': '/wEPDwUKLTc1MTM2NTYzOQ9kFgJmD2QWAgIDD2QWEgIFDw8WAh4EVGV4dAWeDlNwZWNpYWxseSBEZXNpZ25hdGVkIE5hdGlvbmFscyBhbmQgQmxvY2tlZCBQZXJzb25zIGxpc3QgKCJTRE4gTGlzdCIpIGFuZCBhbGwgb3RoZXIgc2FuY3Rpb25zIGxpc3RzIGFkbWluaXN0ZXJlZCBieSBPRkFDLCBpbmNsdWRpbmcgdGhlIEZvcmVpZ24gU2FuY3Rpb25zIEV2YWRlcnMgTGlzdCwgdGhlIE5vbi1TRE4gSXJhbiBTYW5jdGlvbnMgQWN0IExpc3QsIHRoZSBTZWN0b3JhbCBTYW5jdGlvbnMgSWRlbnRpZmljYXRpb25zIExpc3QsIHRoZSBMaXN0IG9mIEZvcmVpZ24gRmluYW5jaWFsIEluc3RpdHV0aW9ucyBTdWJqZWN0IHRvIENvcnJlc3BvbmRlbnQgQWNjb3VudCBvciBQYXlhYmxlLVRocm91Z2ggQWNjb3VudCBTYW5jdGlvbnMgYW5kIHRoZSBOb24tU0ROIFBhbGVzdGluaWFuIExlZ2lzbGF0aXZlIENvdW5jaWwgTGlzdC4gR2l2ZW4gdGhlIG51bWJlciBvZiBsaXN0cyB0aGF0IG5vdyByZXNpZGUgaW4gdGhlIFNhbmN0aW9ucyBMaXN0IFNlYXJjaCB0b29sLCBpdCBpcyBzdHJvbmdseSByZWNvbW1lbmRlZCB0aGF0IHVzZXJzIHBheSBjbG9zZSBhdHRlbnRpb24gdG8gdGhlIHByb2dyYW0gY29kZXMgYXNzb2NpYXRlZCB3aXRoIGVhY2ggcmV0dXJuZWQgcmVjb3JkLiBUaGVzZSBwcm9ncmFtIGNvZGVzIGluZGljYXRlIGhvdyBhIHRydWUgaGl0IG9uIGEgcmV0dXJuZWQgdmFsdWUgc2hvdWxkIGJlIHRyZWF0ZWQuIFRoZSBTYW5jdGlvbnMgTGlzdCBTZWFyY2ggdG9vbCB1c2VzIGFwcHJveGltYXRlIHN0cmluZyBtYXRjaGluZyB0byBpZGVudGlmeSBwb3NzaWJsZSBtYXRjaGVzIGJldHdlZW4gd29yZCBvciBjaGFyYWN0ZXIgc3RyaW5ncyBhcyBlbnRlcmVkIGludG8gU2FuY3Rpb25zIExpc3QgU2VhcmNoLCBhbmQgYW55IG5hbWUgb3IgbmFtZSBjb21wb25lbnQgYXMgaXQgYXBwZWFycyBvbiB0aGUgU0ROIExpc3QgYW5kL29yIHRoZSB2YXJpb3VzIG90aGVyIHNhbmN0aW9ucyBsaXN0cy4gU2FuY3Rpb25zIExpc3QgU2VhcmNoIGhhcyBhIHNsaWRlci1iYXIgdGhhdCBtYXkgYmUgdXNlZCB0byBzZXQgYSB0aHJlc2hvbGQgKGkuZS4sIGEgY29uZmlkZW5jZSByYXRpbmcpIGZvciB0aGUgY2xvc2VuZXNzIG9mIGFueSBwb3RlbnRpYWwgbWF0Y2ggcmV0dXJuZWQgYXMgYSByZXN1bHQgb2YgYSB1c2VyJ3Mgc2VhcmNoLiBTYW5jdGlvbnMgTGlzdCBTZWFyY2ggd2lsbCBkZXRlY3QgY2VydGFpbiBtaXNzcGVsbGluZ3Mgb3Igb3RoZXIgaW5jb3JyZWN0bHkgZW50ZXJlZCB0ZXh0LCBhbmQgd2lsbCByZXR1cm4gbmVhciwgb3IgcHJveGltYXRlLCBtYXRjaGVzLCBiYXNlZCBvbiB0aGUgY29uZmlkZW5jZSByYXRpbmcgc2V0IGJ5IHRoZSB1c2VyIHZpYSB0aGUgc2xpZGVyLWJhci4gT0ZBQyBkb2VzIG5vdCBwcm92aWRlIHJlY29tbWVuZGF0aW9ucyB3aXRoIHJlZ2FyZCB0byB0aGUgYXBwcm9wcmlhdGVuZXNzIG9mIGFueSBzcGVjaWZpYyBjb25maWRlbmNlIHJhdGluZy4gU2FuY3Rpb25zIExpc3QgU2VhcmNoIGlzIG9uZSB0b29sIG9mZmVyZWQgdG8gYXNzaXN0IHVzZXJzIGluIHV0aWxpemluZyB0aGUgU0ROIExpc3QgYW5kL29yIHRoZSB2YXJpb3VzIG90aGVyIHNhbmN0aW9ucyBsaXN0czsgdXNlIG9mIFNhbmN0aW9ucyBMaXN0IFNlYXJjaCBpcyBub3QgYSBzdWJzdGl0dXRlIGZvciB1bmRlcnRha2luZyBhcHByb3ByaWF0ZSBkdWUgZGlsaWdlbmNlLiBUaGUgdXNlIG9mIFNhbmN0aW9ucyBMaXN0IFNlYXJjaCBkb2VzIG5vdCBsaW1pdCBhbnkgY3JpbWluYWwgb3IgY2l2aWwgbGlhYmlsaXR5IGZvciBhbnkgYWN0IHVuZGVydGFrZW4gYXMgYSByZXN1bHQgb2YsIG9yIGluIHJlbGlhbmNlIG9uLCBzdWNoIHVzZS5kZAIHDw8WAh4LTmF2aWdhdGVVcmwFeWh0dHBzOi8vaG9tZS50cmVhc3VyeS5nb3YvcG9saWN5LWlzc3Vlcy9maW5hbmNpYWwtc2FuY3Rpb25zL3NwZWNpYWxseS1kZXNpZ25hdGVkLW5hdGlvbmFscy1saXN0LWRhdGEtZm9ybWF0cy1kYXRhLXNjaGVtYXNkZAIJDw8WAh8BBURodHRwczovL2hvbWUudHJlYXN1cnkuZ292L3BvbGljeS1pc3N1ZXMvZmluYW5jaWFsLXNhbmN0aW9ucy9mYXFzLzI4N2RkAgsPDxYCHwEFa2h0dHBzOi8vaG9tZS50cmVhc3VyeS5nb3YvcG9saWN5LWlzc3Vlcy9vZmZpY2Utb2YtZm9yZWlnbi1hc3NldHMtY29udHJvbC1zYW5jdGlvbnMtcHJvZ3JhbXMtYW5kLWluZm9ybWF0aW9uZGQCDQ8PFgIfAQViaHR0cHM6Ly9ob21lLnRyZWFzdXJ5Lmdvdi9wb2xpY3ktaXNzdWVzL2ZpbmFuY2lhbC1zYW5jdGlvbnMvY29uc29saWRhdGVkLXNhbmN0aW9ucy1saXN0LWRhdGEtZmlsZXNkZAIPDw8WAh8BBZkBaHR0cHM6Ly9ob21lLnRyZWFzdXJ5Lmdvdi9wb2xpY3ktaXNzdWVzL2ZpbmFuY2lhbC1zYW5jdGlvbnMvc3BlY2lhbGx5LWRlc2lnbmF0ZWQtbmF0aW9uYWxzLWxpc3Qtc2RuLWxpc3QvcHJvZ3JhbS10YWctZGVmaW5pdGlvbnMtZm9yLW9mYWMtc2FuY3Rpb25zLWxpc3RzZGQCEQ9kFgQCBQ9kFggCAw8QDxYCHgtfIURhdGFCb3VuZGdkEBUFA0FsbAhBaXJjcmFmdAZFbnRpdHkKSW5kaXZpZHVhbAZWZXNzZWwVBQAIQWlyY3JhZnQGRW50aXR5CkluZGl2aWR1YWwGVmVzc2VsFCsDBWdnZ2dnZGQCGw8QDxYCHwJnZBAVTANBbGwLNTYxLVJlbGF0ZWQHQkFMS0FOUw9CQUxLQU5TLUVPMTQwMzMHQkVMQVJVUw9CRUxBUlVTLUVPMTQwMzgNQlVSTUEtRU8xNDAxNA1DQUFUU0EgLSBJUkFOD0NBQVRTQSAtIFJVU1NJQQNDQVIMQ01JQy1FTzEzOTU5BENVQkEGQ1lCRVIyBkRBUkZVUgREUFJLBURQUksyBURQUkszBURQUks0C0RQUkstTktTUEVBB0RSQ09OR08QRUxFQ1RJT04tRU8xMzg0OBBFVEhJT1BJQS1FTzE0MDQ2BkZTRS1JUgNGVE8GR0xPTUFHBkhJRlBBQQpISy1FTzEzOTM2B0hSSVQtSVIHSFJJVC1TWQRJRkNBBElGU1IVSUxMSUNJVC1EUlVHUy1FTzE0MDU5BElSQU4QSVJBTi1DT04tQVJNUy1FTwxJUkFOLUVPMTM4NDYMSVJBTi1FTzEzODcxDElSQU4tRU8xMzg3NgxJUkFOLUVPMTM5MDIHSVJBTi1IUghJUkFOLVRSQQVJUkFRMgVJUkFRMwRJUkdDA0lTQQdMRUJBTk9OBkxJQllBMgZMSUJZQTMGTUFHTklUDE1BTEktRU8xMzg4MglOSUNBUkFHVUEPTklDQVJBR1VBLU5IUkFBBU5QV01EBk5TLVBMQwVQRUVTQQ1QRUVTQS1FTzE0MDM5DlJVU1NJQS1FTzE0MDI0DlJVU1NJQS1FTzE0MDY1BFNER1QEU0ROVAVTRE5USwdTT01BTElBC1NPVVRIIFNVREFOBlNTSURFUwVTWVJJQQxTWVJJQS1DQUVTQVINU1lSSUEtRU8xMzg5NANUQ08PVUtSQUlORS1FTzEzNjYwD1VLUkFJTkUtRU8xMzY2MQ9VS1JBSU5FLUVPMTM2NjIPVUtSQUlORS1FTzEzNjg1CVZFTkVaVUVMQRFWRU5FWlVFTEEtRU8xMzg1MBFWRU5FWlVFTEEtRU8xMzg4NAVZRU1FTghaSU1CQUJXRRVMAAs1NjEtUmVsYXRlZAdCQUxLQU5TD0JBTEtBTlMtRU8xNDAzMwdCRUxBUlVTD0JFTEFSVVMtRU8xNDAzOA1CVVJNQS1FTzE0MDE0DUNBQVRTQSAtIElSQU4PQ0FBVFNBIC0gUlVTU0lBA0NBUgxDTUlDLUVPMTM5NTkEQ1VCQQZDWUJFUjIGREFSRlVSBERQUksFRFBSSzIFRFBSSzMFRFBSSzQLRFBSSy1OS1NQRUEHRFJDT05HTxBFTEVDVElPTi1FTzEzODQ4EEVUSElPUElBLUVPMTQwNDYGRlNFLUlSA0ZUTwZHTE9NQUcGSElGUEFBCkhLLUVPMTM5MzYHSFJJVC1JUgdIUklULVNZBElGQ0EESUZTUhVJTExJQ0lULURSVUdTLUVPMTQwNTkESVJBThBJUkFOLUNPTi1BUk1TLUVPDElSQU4tRU8xMzg0NgxJUkFOLUVPMTM4NzEMSVJBTi1FTzEzODc2DElSQU4tRU8xMzkwMgdJUkFOLUhSCElSQU4tVFJBBUlSQVEyBUlSQVEzBElSR0MDSVNBB0xFQkFOT04GTElCWUEyBkxJQllBMwZNQUdOSVQMTUFMSS1FTzEzODgyCU5JQ0FSQUdVQQ9OSUNBUkFHVUEtTkhSQUEFTlBXTUQGTlMtUExDBVBFRVNBDVBFRVNBLUVPMTQwMzkOUlVTU0lBLUVPMTQwMjQOUlVTU0lBLUVPMTQwNjUEU0RHVARTRE5UBVNETlRLB1NPTUFMSUELU09VVEggU1VEQU4GU1NJREVTBVNZUklBDFNZUklBLUNBRVNBUg1TWVJJQS1FTzEzODk0A1RDTw9VS1JBSU5FLUVPMTM2NjAPVUtSQUlORS1FTzEzNjYxD1VLUkFJTkUtRU8xMzY2Mg9VS1JBSU5FLUVPMTM2ODUJVkVORVpVRUxBEVZFTkVaVUVMQS1FTzEzODUwEVZFTkVaVUVMQS1FTzEzODg0BVlFTUVOCFpJTUJBQldFFCsDTGdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIhDxAPFgIfAmdkEBW0AQNBbGwLQWZnaGFuaXN0YW4HQWxiYW5pYQdBbGdlcmlhBkFuZ29sYQlBcmdlbnRpbmEHQXJtZW5pYQVBcnViYQlBdXN0cmFsaWEHQXVzdHJpYQpBemVyYmFpamFuDEJhaGFtYXMsIFRoZQdCYWhyYWluCkJhbmdsYWRlc2gIQmFyYmFkb3MHQmVsYXJ1cwdCZWxnaXVtBkJlbGl6ZQVCZW5pbgdCZXJtdWRhB0JvbGl2aWEWQm9zbmlhIGFuZCBIZXJ6ZWdvdmluYQZCcmF6aWwGQnJ1bmVpCEJ1bGdhcmlhDEJ1cmtpbmEgRmFzbwVCdXJtYQhDYW1ib2RpYQZDYW5hZGEOQ2F5bWFuIElzbGFuZHMYQ2VudHJhbCBBZnJpY2FuIFJlcHVibGljBUNoaWxlBUNoaW5hCENvbG9tYmlhB0NvbW9yb3MhQ29uZ28sIERlbW9jcmF0aWMgUmVwdWJsaWMgb2YgdGhlFkNvbmdvLCBSZXB1YmxpYyBvZiB0aGUKQ29zdGEgUmljYQ1Db3RlIGQgSXZvaXJlB0Nyb2F0aWEEQ3ViYQZDeXBydXMOQ3plY2ggUmVwdWJsaWMHRGVubWFyawhEb21pbmljYRJEb21pbmljYW4gUmVwdWJsaWMHRWN1YWRvcgVFZ3lwdAtFbCBTYWx2YWRvchFFcXVhdG9yaWFsIEd1aW5lYQdFcml0cmVhB0VzdG9uaWEIRXRoaW9waWEHRmlubGFuZAZGcmFuY2UHR2VvcmdpYQdHZXJtYW55BUdoYW5hCUdpYnJhbHRhcgZHcmVlY2UJR3VhdGVtYWxhCEd1ZXJuc2V5Bkd1aW5lYQZHdXlhbmEFSGFpdGkISG9uZHVyYXMJSG9uZyBLb25nB0h1bmdhcnkFSW5kaWEJSW5kb25lc2lhBElyYW4ESXJhcQdJcmVsYW5kBklzcmFlbAVJdGFseQdKYW1haWNhBUphcGFuBkplcnNleQZKb3JkYW4KS2F6YWtoc3RhbgVLZW55YQxLb3JlYSwgTm9ydGgMS29yZWEsIFNvdXRoBktvc292bwZLdXdhaXQKS3lyZ3l6c3RhbgRMYW9zBkxhdHZpYQdMZWJhbm9uB0xpYmVyaWEFTGlieWENTGllY2h0ZW5zdGVpbgpMdXhlbWJvdXJnBU1hY2F1CE1hbGF5c2lhCE1hbGRpdmVzBE1hbGkFTWFsdGEQTWFyc2hhbGwgSXNsYW5kcwpNYXVyaXRhbmlhBk1leGljbwdNb2xkb3ZhBk1vbmFjbwhNb25nb2xpYQpNb250ZW5lZ3JvB01vcm9jY28KTW96YW1iaXF1ZQdOYW1pYmlhC05ldGhlcmxhbmRzFE5ldGhlcmxhbmRzIEFudGlsbGVzC05ldyBaZWFsYW5kCU5pY2FyYWd1YQVOaWdlcgdOaWdlcmlhIE5vcnRoIE1hY2Vkb25pYSwgVGhlIFJlcHVibGljIG9mBk5vcndheQRPbWFuCFBha2lzdGFuBVBhbGF1C1BhbGVzdGluaWFuBlBhbmFtYQhQYXJhZ3VheQRQZXJ1C1BoaWxpcHBpbmVzBlBvbGFuZAVRYXRhcipSZWdpb246IENvbW1vbndlYWx0aCBvZiBJbmRlcGVuZGVudCBTdGF0ZXMOUmVnaW9uOiBDcmltZWEMUmVnaW9uOiBHYXphE1JlZ2lvbjogS2FmaWEgS2luZ2kVUmVnaW9uOiBOb3J0aGVybiBNYWxpB1JvbWFuaWEGUnVzc2lhBlJ3YW5kYRVTYWludCBLaXR0cyBhbmQgTmV2aXMgU2FpbnQgVmluY2VudCBhbmQgdGhlIEdyZW5hZGluZXMFU2Ftb2EKU2FuIE1hcmlubwxTYXVkaSBBcmFiaWEHU2VuZWdhbAZTZXJiaWEKU2V5Y2hlbGxlcwxTaWVycmEgTGVvbmUJU2luZ2Fwb3JlCFNsb3Zha2lhCFNsb3ZlbmlhB1NvbWFsaWEMU291dGggQWZyaWNhC1NvdXRoIFN1ZGFuBVNwYWluCVNyaSBMYW5rYQVTdWRhbgZTd2VkZW4LU3dpdHplcmxhbmQFU3lyaWEGVGFpd2FuClRhamlraXN0YW4IVGFuemFuaWEIVGhhaWxhbmQKVGhlIEdhbWJpYRNUcmluaWRhZCBhbmQgVG9iYWdvB1R1bmlzaWEGVHVya2V5DFR1cmttZW5pc3RhbgZVZ2FuZGEHVWtyYWluZQx1bmRldGVybWluZWQUVW5pdGVkIEFyYWIgRW1pcmF0ZXMOVW5pdGVkIEtpbmdkb20NVW5pdGVkIFN0YXRlcwdVcnVndWF5ClV6YmVraXN0YW4HVmFudWF0dQlWZW5lenVlbGEHVmlldG5hbRdWaXJnaW4gSXNsYW5kcywgQnJpdGlzaAlXZXN0IEJhbmsFWWVtZW4GWmFtYmlhCFppbWJhYndlFbQBAAtBZmdoYW5pc3RhbgdBbGJhbmlhB0FsZ2VyaWEGQW5nb2xhCUFyZ2VudGluYQdBcm1lbmlhBUFydWJhCUF1c3RyYWxpYQdBdXN0cmlhCkF6ZXJiYWlqYW4MQmFoYW1hcywgVGhlB0JhaHJhaW4KQmFuZ2xhZGVzaAhCYXJiYWRvcwdCZWxhcnVzB0JlbGdpdW0GQmVsaXplBUJlbmluB0Jlcm11ZGEHQm9saXZpYRZCb3NuaWEgYW5kIEhlcnplZ292aW5hBkJyYXppbAZCcnVuZWkIQnVsZ2FyaWEMQnVya2luYSBGYXNvBUJ1cm1hCENhbWJvZGlhBkNhbmFkYQ5DYXltYW4gSXNsYW5kcxhDZW50cmFsIEFmcmljYW4gUmVwdWJsaWMFQ2hpbGUFQ2hpbmEIQ29sb21iaWEHQ29tb3JvcyFDb25nbywgRGVtb2NyYXRpYyBSZXB1YmxpYyBvZiB0aGUWQ29uZ28sIFJlcHVibGljIG9mIHRoZQpDb3N0YSBSaWNhDUNvdGUgZCBJdm9pcmUHQ3JvYXRpYQRDdWJhBkN5cHJ1cw5DemVjaCBSZXB1YmxpYwdEZW5tYXJrCERvbWluaWNhEkRvbWluaWNhbiBSZXB1YmxpYwdFY3VhZG9yBUVneXB0C0VsIFNhbHZhZG9yEUVxdWF0b3JpYWwgR3VpbmVhB0VyaXRyZWEHRXN0b25pYQhFdGhpb3BpYQdGaW5sYW5kBkZyYW5jZQdHZW9yZ2lhB0dlcm1hbnkFR2hhbmEJR2licmFsdGFyBkdyZWVjZQlHdWF0ZW1hbGEIR3Vlcm5zZXkGR3VpbmVhBkd1eWFuYQVIYWl0aQhIb25kdXJhcwlIb25nIEtvbmcHSHVuZ2FyeQVJbmRpYQlJbmRvbmVzaWEESXJhbgRJcmFxB0lyZWxhbmQGSXNyYWVsBUl0YWx5B0phbWFpY2EFSmFwYW4GSmVyc2V5BkpvcmRhbgpLYXpha2hzdGFuBUtlbnlhDEtvcmVhLCBOb3J0aAxLb3JlYSwgU291dGgGS29zb3ZvBkt1d2FpdApLeXJneXpzdGFuBExhb3MGTGF0dmlhB0xlYmFub24HTGliZXJpYQVMaWJ5YQ1MaWVjaHRlbnN0ZWluCkx1eGVtYm91cmcFTWFjYXUITWFsYXlzaWEITWFsZGl2ZXMETWFsaQVNYWx0YRBNYXJzaGFsbCBJc2xhbmRzCk1hdXJpdGFuaWEGTWV4aWNvB01vbGRvdmEGTW9uYWNvCE1vbmdvbGlhCk1vbnRlbmVncm8HTW9yb2NjbwpNb3phbWJpcXVlB05hbWliaWELTmV0aGVybGFuZHMUTmV0aGVybGFuZHMgQW50aWxsZXMLTmV3IFplYWxhbmQJTmljYXJhZ3VhBU5pZ2VyB05pZ2VyaWEgTm9ydGggTWFjZWRvbmlhLCBUaGUgUmVwdWJsaWMgb2YGTm9yd2F5BE9tYW4IUGFraXN0YW4FUGFsYXULUGFsZXN0aW5pYW4GUGFuYW1hCFBhcmFndWF5BFBlcnULUGhpbGlwcGluZXMGUG9sYW5kBVFhdGFyKlJlZ2lvbjogQ29tbW9ud2VhbHRoIG9mIEluZGVwZW5kZW50IFN0YXRlcw5SZWdpb246IENyaW1lYQxSZWdpb246IEdhemETUmVnaW9uOiBLYWZpYSBLaW5naRVSZWdpb246IE5vcnRoZXJuIE1hbGkHUm9tYW5pYQZSdXNzaWEGUndhbmRhFVNhaW50IEtpdHRzIGFuZCBOZXZpcyBTYWludCBWaW5jZW50IGFuZCB0aGUgR3JlbmFkaW5lcwVTYW1vYQpTYW4gTWFyaW5vDFNhdWRpIEFyYWJpYQdTZW5lZ2FsBlNlcmJpYQpTZXljaGVsbGVzDFNpZXJyYSBMZW9uZQlTaW5nYXBvcmUIU2xvdmFraWEIU2xvdmVuaWEHU29tYWxpYQxTb3V0aCBBZnJpY2ELU291dGggU3VkYW4FU3BhaW4JU3JpIExhbmthBVN1ZGFuBlN3ZWRlbgtTd2l0emVybGFuZAVTeXJpYQZUYWl3YW4KVGFqaWtpc3RhbghUYW56YW5pYQhUaGFpbGFuZApUaGUgR2FtYmlhE1RyaW5pZGFkIGFuZCBUb2JhZ28HVHVuaXNpYQZUdXJrZXkMVHVya21lbmlzdGFuBlVnYW5kYQdVa3JhaW5lDHVuZGV0ZXJtaW5lZBRVbml0ZWQgQXJhYiBFbWlyYXRlcw5Vbml0ZWQgS2luZ2RvbQ1Vbml0ZWQgU3RhdGVzB1VydWd1YXkKVXpiZWtpc3RhbgdWYW51YXR1CVZlbmV6dWVsYQdWaWV0bmFtF1ZpcmdpbiBJc2xhbmRzLCBCcml0aXNoCVdlc3QgQmFuawVZZW1lbgZaYW1iaWEIWmltYmFid2UUKwO0AWdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAiMPEA8WAh8CZ2QQFQMDQWxsB05vbi1TRE4DU0ROFQMAB05vbi1TRE4DU0ROFCsDA2dnZ2RkAgkPZBYCAgUPPCsAEQIBEBYAFgAWAAwUKwAAZAITDw8WAh8ABS5TRE4gTGlzdCBsYXN0IHVwZGF0ZWQgb246IDEvMjYvMjAyMyA3OjAyOjA3IEFNZGQCFQ8PFgIfAAUzTm9uLVNETiBMaXN0IGxhc3QgdXBkYXRlZCBvbjogMTIvMTUvMjAyMiA3OjA3OjE2IEFNZGQYAgUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgMFHmN0bDAwJE1haW5Db250ZW50JEltYWdlQnV0dG9uMgUdY3RsMDAkTWFpbkNvbnRlbnQkbHN0UHJvZ3JhbXMFHmN0bDAwJE1haW5Db250ZW50JEltYWdlQnV0dG9uMQUhY3RsMDAkTWFpbkNvbnRlbnQkZ3ZTZWFyY2hSZXN1bHRzD2dkxNDnaogMTeFKVQWzpIlDwivWJFk=',
        '__VIEWSTATEGENERATOR': 'CA0B0334',
        'ctl00$MainContent$ddlType': '',
        'ctl00$MainContent$txtAddress': '',
        'ctl00$MainContent$txtLastName': keyword,
        'ctl00$MainContent$txtCity': '',
        'ctl00$MainContent$txtID': '',
        'ctl00$MainContent$txtState': '',
        'ctl00$MainContent$lstPrograms': '',
        'ctl00$MainContent$ddlCountry': '',
        'ctl00$MainContent$ddlList': '',
        'ctl00$MainContent$Slider1': '100',
        'ctl00$MainContent$Slider1_Boundcontrol': '100',
        'ctl00$MainContent$btnSearch': 'Search',
    }

    response = requests.post('https://sanctionssearch.ofac.treas.gov/', headers=headers, data=data)


    sublinks=html.fromstring(response.content).xpath("//table[@id='gvSearchResults']//tr/td[1]/a/@href")


    totalAvailable=len(sublinks)
    resultsAll=[]
    outputdict={}
    outputdict['totalAvailable']=totalAvailable


    for sublink in sublinks[0:count]:

        cookies2 = {
            '_gid': 'GA1.2.679650639.1674763855',
            '_ga': 'GA1.1.888145252.1674763855',
            'nmstat': '1a332339-7087-27db-4c86-548d36f20041',
            '_ga_008DHEJFE8': 'GS1.1.1674763855.1.1.1674763876.0.0.0',
            'ASP.NET_SessionId': 'wlrojwfjh3coh1saq25uypoe',
            'BIGipServerEzM5bUtMV5dP4OkrzH904A': '!b+N2ABhLDHeGBu9Ica4I6euaNKjHzqkUsm5Tbvcn2pfWaz4JMPPO++VcKascTVv4BXstypmz43HvSzA=',
            'TS01681a3a': '01f6e3b1e9be7021df9b22797391192e51aa12fdc0386f5205ee8e8eab96a941cfdde1bc83c26236c11c484682928ae178426d503ba98292b94ecacea909bafe1137eaeab3e9a70b7c1b353dac89fc78afe678ad46',
        }

        headers2 = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Language': 'en-CA,en;q=0.9,zh-CA;q=0.8,zh;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Cookie': '_gid=GA1.2.679650639.1674763855; _ga=GA1.1.888145252.1674763855; nmstat=1a332339-7087-27db-4c86-548d36f20041; _ga_008DHEJFE8=GS1.1.1674763855.1.1.1674763876.0.0.0; ASP.NET_SessionId=wlrojwfjh3coh1saq25uypoe; BIGipServerEzM5bUtMV5dP4OkrzH904A=!b+N2ABhLDHeGBu9Ica4I6euaNKjHzqkUsm5Tbvcn2pfWaz4JMPPO++VcKascTVv4BXstypmz43HvSzA=; TS01681a3a=01f6e3b1e9be7021df9b22797391192e51aa12fdc0386f5205ee8e8eab96a941cfdde1bc83c26236c11c484682928ae178426d503ba98292b94ecacea909bafe1137eaeab3e9a70b7c1b353dac89fc78afe678ad46',
            'Pragma': 'no-cache',
            'Referer': 'https://sanctionssearch.ofac.treas.gov/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'dnt': '1',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }



        response2 = requests.get('https://sanctionssearch.ofac.treas.gov/'+sublink, headers=headers2)

        name=(html.fromstring(response2.content).xpath("//span[@id='ctl00_MainContent_lblNameOther']/text()")+[''])[0]
        name_type=(html.fromstring(response2.content).xpath("//span[@id='ctl00_MainContent_lblTypeOther']/text()")+[''])[0]
        name_list=(html.fromstring(response2.content).xpath("//span[@id='ctl00_MainContent_lblSourceListOther']/text()")+[''])[0]
        program=(html.fromstring(response2.content).xpath("//span[@id='ctl00_MainContent_lblProgramOther']/text()")+[''])[0]
        remarks=(html.fromstring(response2.content).xpath("//span[@id='ctl00_MainContent_lblRemarksOther']/text()")+[''])[0]
        secondarySactionRisk=(html.fromstring(response2.content).xpath("//td[contains(text(),'Secondary sanctions risk:')]/following-sibling::td[1]/text()")+[''])[0]

        Aliases=html.fromstring(response2.content).xpath("//table[@id='ctl00_MainContent_gvAliases']/tr")

        alisasList=[]

        for row in Aliases[1:]:
            alias={}
            alias['type']=(row.xpath("./td[1]/text()")+[''])[0]
            alias['category']=(row.xpath("./td[2]/text()")+[''])[0]
            alias['name']=(row.xpath("./td[3]/text()")+[''])[0]
            alisasList.append(alias)

        addresses=html.fromstring(response2.content).xpath("//div[@id='ctl00_MainContent_pnlAddress']/table/tr")

        addressList=[]

        for row in addresses[1:]:
            rowFullText=''.join(row.xpath("./td/text()")).strip()

            if not rowFullText:
                continue
            address={}
            address['street']=(row.xpath("./td[1]/text()")+[''])[0].strip()
            address['city']=(row.xpath("./td[2]/text()")+[''])[0].strip()
            address['state']=(row.xpath("./td[3]/text()")+[''])[0].strip()
            address['Postal Code']=(row.xpath("./td[4]/text()")+[''])[0].strip()
            address['Country']=(row.xpath("./td[5]/text()")+[''])[0].strip()
            addressList.append(address)


        result={}
        result['name']=name
        result['name_type']=name_type
        result['name_list']=name_list
        result['program']=program
        result['remarks']=remarks
        result['secondarySanctionRist']=secondarySactionRisk
        result['Aliases']=alisasList
        result['address']=addressList

        resultsAll.append(result)

    outputdict['results']=resultsAll

    return outputdict





if __name__=='__main__':

    corps=searchOfac('bar')
