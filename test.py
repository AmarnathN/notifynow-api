from bs4 import BeautifulSoup

html = '''<table class="m_3973256846661623402content-shell-table" width="500" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0;background-color:rgb(255,255,255)"> 
       <tbody>
        <tr> 
         <td> 
           <img src="https://ci5.googleusercontent.com/proxy/BTfohqXLNos23tlZxvJ6vj9Uo2qBONyD9ls4bMN5Rd0EbXroXrbGJRj8bxWD9EG0PD3tbl28gdaYqTfzqOxyjg7I8wGBSfYaO575QE6EmIT4wObqXOAPCXOgEFvGqDCD5C2XGlGGrsHg8cEat6wHSFpj8xm35T_U4WisFh3nBvWLvlRwmQlNHxt4bTDaGE2Nvn9VppPFjgkchHUosYFPKf0OPJnU3GRgPTbjeoZnpR-AAC5nMB_xj4jk16jfAhDlMsySKdEWi0gfZlSX8LrMywkYXe_5XMNfvXsFEqiujEKXA8mc5EoVgH1xoa-pPLSyywVLjY3SPzt5Yx6Y8RSoPKIPi3A9rSFvh5dHNlcdZZDNwe7f7He2gKfuATsVIiHpL1OxylVQWxoPOYNIaQ0qddWDrC28zpdq8oMZOwpT9WKk_zIbpPwGSKi0NifyQjkN6sLwCmx9VPYYsA-GhjGzJoLwx8wEyNTCf5Yhn4_d5YmqNWwKtrRQTUaB01FMyxRQ8kFeJjftC-lR_JURRzBvNkEbA9qqS9ny8VJVMQtk_Tuz00Wk8vbedYVoAcmY2kcTFUdX2B2h2Xz4K4CLIDVcn36OtCwYZOI7QDe6BFH2c7MizAhUEH_RTLmp9Z4e3033wWqrRdnwWHsn67_pLW8A2Ka4JmXMyvoB0uOGAVuk3Y50wIHjuky8i5vEEjvlbeOKImWaUMg1hielbJXwSHa9Zymeme0q3-W0EyQV=s0-d-e1-ft#http://beacon.netflix.com/img/BAQgBEAEa8AJ2THSsgosiINnMMOKPnivWe5huhHkmJuaTYxkT0AOLCwZNaoQGqGQfQW1G0vTYWloMbuDlH-l7AQLDUHCFbvWgWVruDNAnG_3dkdQWB2oOK5lCPmvzcBlcCCjnos6Hjm8PyetdNWLfaHBuph7N8esspcz_s_4e6bpYBAUBoK5ymJTLzft-hvV5VoxmhdMjqLVl2uFyz9DPCBaqjGd-IAx2qot0DofdQgK1aj9Lk9O-uV3SQnEJvoGuyh2VyWcS_9UqJIAD8Ui93vjZCnFubNwuivbi5BhokkXj-9f0T_khoWvn5wv03Rym8ZM-Si6knx3ADzqIR23AYtziZlnl39iTrBZglBg8rdH_78_vWyUPBc0Zm0S8T85EQdCVJNreC-kgptp0xxT3FyvIUHwsFpC7l4pwP2TrBRfk5oCibsjGg4OQvk9TBNyOiO6w8gzEBN8RFEaqlEXuCa6JDdcier5f03Km5tqFtkNWQVOu3hi-KA.." style="display:block;border:none;outline:none;border-collapse:collapse" border="0" class="CToWUd"> </td> 
        </tr> 
         
        <tr> 
         <td class="m_3973256846661623402content-shell" align="center"> 
          <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
           <tbody>
            <tr> 
             <td class="m_3973256846661623402content-padding" style="padding-top:20px;padding-left:20px;padding-right:20px" align="left"> 
              <table cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
               <tbody>
                <tr> 
                 <td> <a href="https://www.netflix.com/browse?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_HOME" style="color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/browse?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_HOME&amp;source=gmail&amp;ust=1595167110340000&amp;usg=AFQjCNGD5S2Q1PRrn95F08BVCZPLdzWPQw"> <img alt="Netflix" src="https://ci3.googleusercontent.com/proxy/9A3a1TA6Bh0RAmVqtdE5P9Z8SdpMQsxFBej9freij52Jz3U4dG4idTHySBCwWROmaNIXVmM2bO1Ewgzn23JDu7yUnw=s0-d-e1-ft#https://assets.nflxext.com/us/email/gem/nflx.png" width="24" border="0" style="border:none;outline:none;border-collapse:collapse;border-style:none" class="CToWUd"> </a> </td> 
                 <td class="m_3973256846661623402gem-header-copy-cell" style="padding:0 0 3px 20px"> 
                  <table cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
                   <tbody>
                    <tr> 
                     <td id="m_3973256846661623402gem-header-copy" class="m_3973256846661623402gem-h4" style="color:#000000;font-family:NetflixSans-Bold,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;font-size:18px;line-height:22px;letter-spacing:-0.35px"> For Navuluri </td> 
                    </tr> 
                   </tbody>
                  </table> </td> 
                </tr> 
               </tbody>
              </table> </td> 
            </tr> 
           </tbody>
          </table> 
          <table class="m_3973256846661623402gem-module-title-card-table" align="center" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
           <tbody>
            <tr> 
             <td class="m_3973256846661623402content-padding" style="padding-top:20px;padding-left:20px;padding-right:20px" align="center"> 
              <table class="m_3973256846661623402outer-radius" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0;border-radius:8px"> 
               <tbody>
                <tr> 
                 <td> 
                  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
                   <tbody>
                    <tr> 
                     <td class="m_3973256846661623402gem-component-image-cell" align="center" style="padding-top:0px"> <a href="https://www.netflix.com/title/81267632?trkid=13710079&amp;MSG_TITLE=81267632&amp;lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=PRIMARY_HERO_IMAGE" style="color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/title/81267632?trkid%3D13710079%26MSG_TITLE%3D81267632%26lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DPRIMARY_HERO_IMAGE&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNErAzO4nASFitepO-CkY4HvkDdqKw"> <img alt="Strangers from Hell" src="https://ci4.googleusercontent.com/proxy/OSYZ_MxZUgRBO-4oGOOXviqFCKgL1GlnH2aAF6rFRADKAWJedZw-EM1nly3RNF_6UbAr4FzT78cEgD27npr2eSRdI0o9QdVEcIksFPze-bZVqa1PEsXlF7PvTP9c4yVLZY3Y87OJ74RAH6gdD_z-NjtXucy4EtUf4GJKDNKPvQArK2IqsTpVikkU6Xwo8eO9Dvw1o6vre4hTpekeMIjk1Vc3Q8uINnebieX6wsCnRcrPOITJsnBfp_LxOysNGYVdtCPJvu719IaKopHRHJTnaOD7PWk=s0-d-e1-ft#https://dnm.nflximg.net/api/v6/X194eJsgWBDE2aQbaNdmCXGUP-Y/AAAACySgNkDq_qyTVy6UlBrGGWss41ixi84zCka73CaaXrSIDUtlj9Z50obUMV15PzoO-OzGzd3CkKjcV7Lwo_GNkGP37sh8oxQrd-cxWyB-FL6iy0CJHsnitLs.jpg?r=07f" width="460" border="0" style="border-radius:8px 8px 0px 0px;max-width:460px;display:block;border:none;outline:none;border-collapse:collapse;border-style:none" class="CToWUd"> </a> </td> 
                    </tr> 
                   </tbody>
                  </table> 
                  <table class="m_3973256846661623402gem-module-top-picks-cell-inner-table" align="center" width="100%" bgcolor="#000000" style="border-radius:0px 0px 8px 8px;border-spacing:0" cellpadding="0" cellspacing="0" border="0"> 
                   <tbody>
                    <tr> 
                     <td class="m_3973256846661623402gem-module-top-picks-body-cell m_3973256846661623402inner-padding" style="padding-left:20px;padding-right:20px;padding-top:20px;padding-bottom:20px"> 
                      <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
                       <tbody>
                        <tr> 
                         <td class="m_3973256846661623402gem-h4" align="left" style="color:#ffffff;font-family:NetflixSans-Bold,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;font-size:18px;line-height:22px;letter-spacing:-0.35px"> Strangers from Hell </td> 
                        </tr> 
                        <tr> 
                         <td class="m_3973256846661623402gem-p1" align="left" style="color:#221f1f;padding-top:12px;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:300;font-size:14px;line-height:18px;letter-spacing:-0.25px"> <span class="m_3973256846661623402gem-element-round-container" style="border:1px solid #434344;color:#f5f5f1;background-color:#434344;padding:2px 4px 2px 4px;border-radius:4px">2019</span> &nbsp; <span class="m_3973256846661623402gem-element-round-container" style="border:1px solid #434344;color:#f5f5f1;background-color:#434344;padding:2px 4px 2px 4px;border-radius:4px">18+</span> &nbsp; <span class="m_3973256846661623402gem-element-round-container" style="border:1px solid #434344;color:#f5f5f1;background-color:#434344;padding:2px 4px 2px 4px;border-radius:4px">10 Episodes</span> </td> 
                        </tr> 
                        <tr> 
                         <td class="m_3973256846661623402gem-p1" align="left" style="color:#f5f5f1;padding-top:12px;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:300;font-size:14px;line-height:18px;letter-spacing:-0.25px"> Unpleasant events disturb the life of an aspiring crime fiction writer when he becomes a resident of an apartment building teeming with shady neighbors.&nbsp;&nbsp; <a href="https://www.netflix.com/title/81267632?trkid=13710079&amp;MSG_TITLE=81267632&amp;lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=PRIMARY_MORE_INFO" style="color:#f5f5f1;text-decoration:underline;color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/title/81267632?trkid%3D13710079%26MSG_TITLE%3D81267632%26lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DPRIMARY_MORE_INFO&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNGdF0-fgK6p7mAAnVb9z8W9TRz9BA">More&nbsp;Info</a> </td> 
                        </tr> 
                       </tbody>
                      </table> 
                      <table class="m_3973256846661623402gem-dual-buttons-table" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
                       <tbody>
                        <tr> 
                         <td style="padding-top:20px" align="center"> 
                          <table class="m_3973256846661623402gem-dual-buttons-table" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
                           <tbody>
                            <tr> 
                             <td width="48%"> 
                              <table class="m_3973256846661623402gem-dual-buttons" bgcolor="#e50914" style="border:solid 2px #e50914;border-radius:4px;text-decoration:none;width:100%;border-spacing:0" cellpadding="0" cellspacing="0" border="0"> 
                               <tbody>
                                <tr> 
                                 <td class="m_3973256846661623402gem-h5 m_3973256846661623402gem-button-copy" style="color:#f5f5f1;font-family:NetflixSans-Bold,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;font-size:14px;line-height:17px;letter-spacing:-0.2px" align="center" height="42"> <a href="https://www.netflix.com/watch/81267632?trkid=13710079&amp;MSG_TITLE=81267632&amp;lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=PRIMARY_PLAY_CTA" style="color:#f5f5f1;text-decoration:none;color:inherit;padding:13px 40px;text-align:center;display:inline-block" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/watch/81267632?trkid%3D13710079%26MSG_TITLE%3D81267632%26lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DPRIMARY_PLAY_CTA&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNFEH_GAR3DhFuIsFHxJ_NGw4kuJ2w"> <img src="https://ci3.googleusercontent.com/proxy/-5pECNMLsjHpgfGmDtwWKOZ6hpXOkZ96G2EuHkobFXw10tVbPaGacJg8QjqEt3v2bLJKIGiGUhI5xpvgX4TO0SoXKIM4PWuu-KB9hhxK0mOrgZqe=s0-d-e1-ft#https://assets.nflxext.com/us/email/gem/icons/icon_play_white.png" height="11" border="0" style="display:inline;height:11px;border:none;outline:none;border-collapse:collapse;border-style:none" class="CToWUd">&nbsp;Play </a> </td> 
                                </tr> 
                               </tbody>
                              </table> </td> 
                             <td width="3%"> <img src="https://ci5.googleusercontent.com/proxy/xLXYddJNri3CltDx_z52vktI7WhijE_ufeIyS323p0HlD1lKUTzUsVfR-LrSh2oPk1SYJb0Z7VTRMPkF5W3LvvE=s0-d-e1-ft#https://assets.nflxext.com/us/email/spacer.gif" width="3%" style="border:none;outline:none;border-collapse:collapse" class="CToWUd"> </td> 
                             <td width="48%"> 
                              <table class="m_3973256846661623402gem-dual-buttons" bgcolor="#333333" style="border:solid 2px #333333;border-radius:4px;text-decoration:none;width:100%;border-spacing:0" cellpadding="0" cellspacing="0" border="0"> 
                               <tbody>
                                <tr> 
                                 <td class="m_3973256846661623402gem-h5 m_3973256846661623402gem-button-copy" style="color:#f5f5f1;font-family:NetflixSans-Bold,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;font-size:14px;line-height:17px;letter-spacing:-0.2px" align="center" height="42"> <a href="https://www.netflix.com/add/81267632?msg_token=EQIAmQABAYEASuitnKSphUe7F%2F8Z6yKGlGIHWPMTZV4JPBoTBDBzWLX8WBnedbh6qhmH3AFuL5yWi%2B04YJkAsVRhHB8hygIVhe04Px8PMD6pHIFP4lY%2FWC%2Fnc830GkHaz%2BY2dD3opLsAiT9dsSR7aY1U%2FWOCXGwNB895soFbTmUFwDi3YU7ZYu2950VZlHqq30dc41%2FSGSWKacr52XmqJUOXoG0hzs2B030mAa74Vg%2Fwj2k%2Bosul%2BCCBy4CJ%2FeqkN3Ls4Scf62ec%2BTM7j%2FxnI9LC6bSQI06dbNoy2v62AYZbMjWQMVfJI%2BC1jJsjgqG018%2BmuWrQBQ4tDOA8xdKJ4fN8jJYT4m4qGkrpmHE%3D&amp;trkid=13710079&amp;MSG_TITLE=81267632&amp;lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=PRIMARY_ADD_CTA" style="color:#f5f5f1;text-decoration:none;color:inherit;padding:13px 40px;text-align:center;display:inline-block" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/add/81267632?msg_token%3DEQIAmQABAYEASuitnKSphUe7F%252F8Z6yKGlGIHWPMTZV4JPBoTBDBzWLX8WBnedbh6qhmH3AFuL5yWi%252B04YJkAsVRhHB8hygIVhe04Px8PMD6pHIFP4lY%252FWC%252Fnc830GkHaz%252BY2dD3opLsAiT9dsSR7aY1U%252FWOCXGwNB895soFbTmUFwDi3YU7ZYu2950VZlHqq30dc41%252FSGSWKacr52XmqJUOXoG0hzs2B030mAa74Vg%252Fwj2k%252Bosul%252BCCBy4CJ%252FeqkN3Ls4Scf62ec%252BTM7j%252FxnI9LC6bSQI06dbNoy2v62AYZbMjWQMVfJI%252BC1jJsjgqG018%252BmuWrQBQ4tDOA8xdKJ4fN8jJYT4m4qGkrpmHE%253D%26trkid%3D13710079%26MSG_TITLE%3D81267632%26lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DPRIMARY_ADD_CTA&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNEhU60rYdVwccZwr24TyNGtWQUfmQ"> + My List </a> </td> 
                                </tr> 
                               </tbody>
                              </table> </td> 
                            </tr> 
                           </tbody>
                          </table> </td> 
                        </tr> 
                       </tbody>
                      </table> </td> 
                    </tr> 
                   </tbody>
                  </table> </td> 
                </tr> 
               </tbody>
              </table> </td> 
            </tr> 
           </tbody>
          </table> 
          <table class="m_3973256846661623402gem-copy-table" align="left" style="width:100%;border-spacing:0" cellpadding="0" cellspacing="0" border="0"> 
           <tbody>
            <tr> 
             <td class="m_3973256846661623402gem-h4 m_3973256846661623402content-padding" align="left" style="padding-top:20px;color:#000000;padding-left:20px;padding-right:20px;font-family:NetflixSans-Bold,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:700;font-size:18px;line-height:22px;letter-spacing:-0.35px"> Recently Added </td> 
            </tr> 
           </tbody>
          </table> 
           
          <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
           <tbody>
            <tr> 
             <td class="m_3973256846661623402spacer" style="padding:8px 0 0 0;font-size:0;line-height:0"> &nbsp; </td> 
            </tr> 
           </tbody>
          </table> 
           
          <table id="m_3973256846661623402gem-title-row-table-table" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
           <tbody>
            <tr> 
             <td class="m_3973256846661623402gem-title-row-td m_3973256846661623402content-padding" style="padding-left:20px;padding-right:20px"> 
              <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
               <tbody>
                <tr> 
                 <td> <a href="https://www.netflix.com/title/80230399?trkid=13710079&amp;MSG_TITLE=80230399&amp;lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=TITLE_ROW_1_BOX_0" style="color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/title/80230399?trkid%3D13710079%26MSG_TITLE%3D80230399%26lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DTITLE_ROW_1_BOX_0&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNHPBMxjDFvX3fuu0B2uWyhhIiu5fQ"> <img alt="Extraction" src="https://ci3.googleusercontent.com/proxy/8rCGIFZTMXuGYW3YQVvG6Gq1Y9apultGe70pVGLi9MoUym58hc5PMqkrfhdsnvwpGqJCCGDnPCB9h1kBZYrPhNuQA8x0MRDXMXIB-E6IXN-_NaJCOupXCpmyiXDno9o7A4V_H2bomMpO2eHd9tHVccb6dLgtRDLVF3YcCDK7aJwNj1T6QqxizoUjBYd65NbE70IktShDwBi4R_arbANS8iAvF4d_ol9IlcmqSQGmWNGflXS8KtnqqposExs2wfnEcoJp-4tphu8DixDc4mQDkBqIfRcC0MxyTGqq=s0-d-e1-ft#https://dnm.nflximg.net/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAACwuDPFFJ-NuA3mmHXPPbzVnb6FD3UF9hNLtC0ZmTnw_8PGeClZ5eZfwNleiJNnIJfV31UDZzMG5xdZ1oAD5JxncmuIErH1-MKKHRajf11hE_fnSrEfZ3aRPNOBLOpA.jpg?r=547" width="149.3333333333" style="border-collapse:collapse;display:block;border-radius:8px;border:none;outline:none;border-collapse:collapse;border-style:none" class="CToWUd"> </a> </td> 
                 <td width="6"> &nbsp; </td> 
                 <td> <a href="https://www.netflix.com/title/81273583?trkid=13710079&amp;MSG_TITLE=81273583&amp;lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=TITLE_ROW_1_BOX_1" style="color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/title/81273583?trkid%3D13710079%26MSG_TITLE%3D81273583%26lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DTITLE_ROW_1_BOX_1&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNHRCTMAFFywk0BHGhgdlPRsVsK5EA"> <img alt="Bheeshma" src="https://ci3.googleusercontent.com/proxy/Q6LUGkIGdtl6Il9XELWd0_B_03yLTRfRmVAN4PVmOU5rPD3MOHFltUaXhDHs4lr1-CM9icsOgwY7di72QfCv_4tlsC0niuZ1Ij8blQmK2FTSQDanyq5LtC2u_YS4S-axrU-xjx4wGG34XM954xLxp0Mme7hwzGGXtqpqBzAgCwYwvNIrX91VR0mJS2UnSPBYSlMveqBjF2q8XYkRLrJXuujqmIv-KykoUzu4DTnwtojD0pMyVfJu81s=s0-d-e1-ft#https://dnm.nflximg.net/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAAC9kJvzj07bAeduB9zJVPUI-fo19Kc0hLUP59llzxZNqvoya2lQU7S0nQBpUALBNaMNQcnumEcXxKnyQM99bzc_zXctGr.jpg?r=d4f" width="149.3333333333" style="border-collapse:collapse;display:block;border-radius:8px;border:none;outline:none;border-collapse:collapse;border-style:none" class="CToWUd"> </a> </td> 
                 <td width="6"> &nbsp; </td> 
                 <td> <a href="https://www.netflix.com/title/80179190?trkid=13710079&amp;MSG_TITLE=80179190&amp;lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=TITLE_ROW_1_BOX_2" style="color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/title/80179190?trkid%3D13710079%26MSG_TITLE%3D80179190%26lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DTITLE_ROW_1_BOX_2&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNFTt4yW00UlHDA6yXPeyGKRCdaP2Q"> <img alt="Never Have I Ever" src="https://ci3.googleusercontent.com/proxy/5KrFhuwPY4Z4Yub8qejNdYOs3mwhZY98LQxAQyOc1HKWJwEtWUq6--tnP9ni17zUZmx7f3z71I4nDnQkB_vLP8IP9UT1WGraKgh_PJRGGpYAlcv2CIVkfij7E1jMP3qyE4r30b9IfQLc92cniz-eiwI7GIRvN__fpnJRkzNFLto48q0kaFr7NC60Z_MVddC7J_AGtZmiJIaACAE5uHq2e_oStVq6w-4mv73Itf2jhJu8i0FzPKtpsnqL4_5fkBciRsgR-7HEEy71EQw1LZaCf15ijpaZwGzX9YDe=s0-d-e1-ft#https://dnm.nflximg.net/api/v6/evlCitJPPCVCry0BZlEFb5-QjKc/AAAAC2fTsVQaWGl9zRYgWm5BtJQphDjunFVgIzuVtz49sV3p8s8xlkyjE39In66aiO5D0xYvkMYgM0Ze6n3cTB_gj6RUD9fcoK5iWQcrO0DlFvSr2tvYzP19wjV5U9j3cA.jpg?r=3d9" width="149.3333333333" style="border-collapse:collapse;display:block;border-radius:8px;border:none;outline:none;border-collapse:collapse;border-style:none" class="CToWUd"> </a> </td> 
                </tr> 
               </tbody>
              </table> </td> 
            </tr> 
           </tbody>
          </table> 
          <table class="m_3973256846661623402gem-single-button-shell m_3973256846661623402button-mobile-flex" width="100%" align="center" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
           <tbody>
            <tr> 
             <td class="m_3973256846661623402gem-single-button m_3973256846661623402content-padding" style="padding-top:20px;padding-left:20px;padding-right:20px" align="center"> 
              <table class="m_3973256846661623402gem-single-button m_3973256846661623402button-1-table" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0;width:100%"> 
               <tbody>
                <tr> 
                 <td class="m_3973256846661623402gem-single-button m_3973256846661623402button-1-text m_3973256846661623402gem-p1 m_3973256846661623402button-text-light" style="background-color:#e50914;border:solid 1px #e50914;color:rgb(255,255,255);font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:300;font-size:14px;line-height:18px;letter-spacing:-0.25px;border-radius:4px;text-decoration:none;text-align:center;padding:13px 0 13px 0;width:100%"> <a class="m_3973256846661623402gem-single-button m_3973256846661623402button-text-light m_3973256846661623402gem-p1" href="https://www.netflix.com/browse?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_HOME_2" style="text-decoration:none;display:block;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:300;font-size:14px;line-height:18px;letter-spacing:-0.25px;color:inherit;color:rgb(255,255,255)" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/browse?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_HOME_2&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNEmy2Os2A6RgU9Lh3Kht3Lp9RKz0g">View All TV Programmes &amp; Films</a> </td> 
                </tr> 
               </tbody>
              </table> </td> 
            </tr> 
           </tbody>
          </table> 
          <table id="m_3973256846661623402gem-footer" class="m_3973256846661623402gem-footer m_3973256846661623402mobile-100w" bgcolor="#ffffff" width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
           <tbody>
            <tr> 
             <td class="m_3973256846661623402content-padding" style="padding-top:40px;padding-left:20px;padding-right:20px"> 
              <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
               <tbody>
                <tr> 
                 <td class="m_3973256846661623402icon" width="1%" valign="top" style="padding-right:22px"> <a href="https://www.netflix.com/browse?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_HOME_3" style="color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/browse?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_HOME_3&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNEgPbTLol0h4bGdMcCYLshewHVGLg"> <img alt="Netflix" src="https://ci3.googleusercontent.com/proxy/9A3a1TA6Bh0RAmVqtdE5P9Z8SdpMQsxFBej9freij52Jz3U4dG4idTHySBCwWROmaNIXVmM2bO1Ewgzn23JDu7yUnw=s0-d-e1-ft#https://assets.nflxext.com/us/email/gem/nflx.png" width="24" border="0" style="border:none;outline:none;border-collapse:collapse;border-style:none" class="CToWUd"> </a> </td> 
                 <td> 
                  <table width="100%" valign="top" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
                   <tbody>
                    <tr> 
                     <td class="m_3973256846661623402gem-p1 m_3973256846661623402questions" style="font-family:NetflixSans-Medium,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:500;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:300;font-size:14px;line-height:18px;letter-spacing:-0.25px;color:rgb(169,166,166)"> Questions? Call 000-800-040-1843 </td> 
                    </tr> 
                    <tr> 
                     <td class="m_3973256846661623402gem-legal m_3973256846661623402address" style="font-size:11px;line-height:14px;letter-spacing:-0.1px;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:300;color:rgb(169,166,166);text-decoration:none;color:rgb(169,166,166);padding-bottom:20px"> <span class="m_3973256846661623402hide-link" style="text-decoration:none;color:rgb(169,166,166)"><a href="https://www.netflix.com/browse?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_HOME_4" style="text-decoration:none;text-decoration:underline;color:rgb(169,166,166);color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/browse?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_HOME_4&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNHlFM1trnyae_48tyF1lYRzu_SIGQ"><span class="il">Netflix</span> Entertainment Services India LLP</a></span> </td> 
                    </tr> 
                    <tr> 
                     <td class="m_3973256846661623402footer-links" style="padding-bottom:20px;color:rgb(169,166,166)"> <a href="https://www.netflix.com/ManageSubscriptions?id=BQE0AAEBEIeEVLa0vCFQ6XZ09jq8H%2FmAkM7sKSUrLoY4rpzbrz2O2m%2B%2FQEfxxeh0x%2Bn%2BPII2oT8e03vLTpsaXvJoJ%2FS3wPrVNXHI%2FeYjMjLSpoClTtO2bwLCbcfyL%2F7P2hcUuwnREKWGdbC2yfZ%2Bt9b96Ey4ZmHOGUtfDzquQ3yISG%2FYp0RJ8qk9FzvdEpPUYehgBOHij8YVW%2BPkpxCVoRfAlkzPLyqnrQ%3D%3D&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;mid=20792311&amp;lkid=URL_UNSUB&amp;lnktrk=EMP" style="font-family:NetflixSans-Medium,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:500;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-size:12px;line-height:20px;text-decoration:underline;color:rgb(169,166,166);color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/ManageSubscriptions?id%3DBQE0AAEBEIeEVLa0vCFQ6XZ09jq8H%252FmAkM7sKSUrLoY4rpzbrz2O2m%252B%252FQEfxxeh0x%252Bn%252BPII2oT8e03vLTpsaXvJoJ%252FS3wPrVNXHI%252FeYjMjLSpoClTtO2bwLCbcfyL%252F7P2hcUuwnREKWGdbC2yfZ%252Bt9b96Ey4ZmHOGUtfDzquQ3yISG%252FYp0RJ8qk9FzvdEpPUYehgBOHij8YVW%252BPkpxCVoRfAlkzPLyqnrQ%253D%253D%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26mid%3D20792311%26lkid%3DURL_UNSUB%26lnktrk%3DEMP&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNHtDpnwVJyuVFYs0uZFfI0U_QIn0g">Unsubscribe</a><br><a href="https://www.netflix.com/TermsOfUse?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_TERMS" style="font-family:NetflixSans-Medium,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:500;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-size:12px;line-height:20px;text-decoration:underline;color:rgb(169,166,166);color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/TermsOfUse?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_TERMS&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNF6GHnVypp3J9s5J9sZVrCq3HzUUQ">Terms of Use</a><br><a href="https://www.netflix.com/PrivacyPolicy?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_PRIVACY" style="font-family:NetflixSans-Medium,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:500;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-size:12px;line-height:20px;text-decoration:underline;color:rgb(169,166,166);color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/PrivacyPolicy?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_PRIVACY&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNHUVxQQkfh041-vUx1j7VAxQBpU2A">Privacy</a><br><a href="https://help.netflix.com/help?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_HELP_3" style="font-family:NetflixSans-Medium,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:500;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-size:12px;line-height:20px;text-decoration:underline;color:rgb(169,166,166);color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://help.netflix.com/help?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_HELP_3&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNGrn6_zENOzopwr4utSq6xGMyGsVA">Help Centre</a> </td> 
                    </tr> 
                    <tr> 
                     <td class="m_3973256846661623402gem-legal" style="font-size:11px;line-height:14px;letter-spacing:-0.1px;font-family:NetflixSans-Light,Helvetica,Roboto,Segoe UI,sans-serif;font-weight:300;color:rgb(169,166,166)"> This message was emailed to <span class="m_3973256846661623402hide-link" style="text-decoration:none;color:rgb(169,166,166)"><a href="https://www.netflix.com/browse?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_HOME_5" style="text-decoration:none;text-decoration:underline;color:rgb(169,166,166);color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://www.netflix.com/browse?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_HOME_5&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNE5Uy7AhR_jfFKoZQke2EfWwvA7pw">[vayuteja@gmail.com]</a></span> by <span class="il">Netflix</span> as part of your <span class="il">Netflix</span>&nbsp;membership.<br> SRC: <a href="https://help.netflix.com/help?lnktrk=EMP&amp;g=589FF4DDB4C7AB948CCAA62119641D416453317D&amp;lkid=URL_HELP_5" class="m_3973256846661623402hide-link" style="text-decoration:none;text-decoration:underline;color:rgb(169,166,166);color:inherit" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://help.netflix.com/help?lnktrk%3DEMP%26g%3D589FF4DDB4C7AB948CCAA62119641D416453317D%26lkid%3DURL_HELP_5&amp;source=gmail&amp;ust=1595167110341000&amp;usg=AFQjCNGrWXnw7jEWCzrabRRo1V_vdzKPrQ">14338_en-GB_IN</a> </td> 
                    </tr> 
                   </tbody>
                  </table> </td> 
                </tr> 
               </tbody>
              </table> 
               
              <table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-spacing:0"> 
               <tbody>
                <tr> 
                 <td class="m_3973256846661623402spacer" style="padding:40px 0 0 0;font-size:0;line-height:0"> &nbsp; </td> 
                </tr> 
               </tbody>
              </table> 
               </td> 
            </tr> 
           </tbody>
          </table> </td> 
        </tr> 
       </tbody>
      </table>'''

soup = BeautifulSoup(html, 'html.parser')

job_elems = soup.select('[class*="-header-copy"]')
print("{} \n hey".format(job_elems[0].get_text().strip().replace("For ","")))



job_elems = soup.select('[class*="-component-image-cell"] a')
print(job_elems[0]['href'])

job_elems = soup.select('[class*="-component-image-cell"] img')
print(job_elems[0]['src'])