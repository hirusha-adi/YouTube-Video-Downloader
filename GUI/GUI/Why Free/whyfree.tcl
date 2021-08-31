#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Aug 31, 2021 09:36:05 AM +0530  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #ffffff 
    wm focusmodel $top passive
    wm geometry $top 604x450+794+247
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4644 1274
    wm minsize $top 117 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "Why Free?"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab46 \
        -background #ffffff -cursor arrow -disabledforeground #a3a3a3 \
        -font "-family {Showcard Gothic} -size 24 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #ff0f15 -text {YouTube Video Downloader} 
    vTcl:DefineAlias "$top.lab46" "LMain" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -activebackground #f9f9f9 -activeforeground black -background #ffffff \
        -disabledforeground #a3a3a3 \
        -font "-family {Sitka Display} -size 20 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #ff0f15 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Why Free?} 
    vTcl:DefineAlias "$top.lab47" "LMain_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab48 \
        -activebackground #f9f9f9 -activeforeground black -background #ffffff \
        -cursor arrow -disabledforeground #a3a3a3 \
        -font "-family {Sitka Display} -size 15 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #ff0f15 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black \
        -text {Once, i tried to download my music playlist to listen locally} 
    vTcl:DefineAlias "$top.lab48" "LMain_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab49 \
        -activebackground #f9f9f9 -activeforeground black -background #ffffff \
        -disabledforeground #a3a3a3 \
        -font {-family {Sitka Display} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ff0f15 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black \
        -text {and the experience was inferior! The only options I had was} 
    vTcl:DefineAlias "$top.lab49" "LMain_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab50 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Sitka Display} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ff0f15 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black \
        -text {to pay 40 USD to purchase that piece of software.... and YES!} 
    vTcl:DefineAlias "$top.lab50" "LMain_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Sitka Display} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ff0f15 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black \
        -text {I didn't do it. I had a great idea of creating} 
    vTcl:DefineAlias "$top.lab51" "LMain_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Sitka Display} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ff0f15 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black \
        -text {a YouTube Video Downloader myself, free and open source!} 
    vTcl:DefineAlias "$top.lab52" "LMain_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Sitka Display} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ff0f15 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black \
        -text {This is not a game changer.. but will get the work done} 
    vTcl:DefineAlias "$top.lab53" "LMain_1_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab54 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Sitka Display} -size 15 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ff0f15 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {Made by ZeaCeR#5641} 
    vTcl:DefineAlias "$top.lab54" "LMain_1_1_1_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but55 \
        -activebackground #93ff51 -activeforeground #000000 \
        -background #fc5c61 -disabledforeground #a3a3a3 \
        -font "-family Uniflex_PersonalUseOnly -size 24 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Go back to Home} 
    vTcl:DefineAlias "$top.but55" "gohome" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab46 \
        -in $top -x 0 -y 0 -width 0 -relwidth 0.99 -height 0 -relheight 0.113 \
        -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.017 -y 0 -rely 0.178 -width 0 -relwidth 0.207 \
        -height 0 -relheight 0.091 -anchor nw -bordermode ignore 
    place $top.lab48 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.289 -width 0 -relwidth 0.79 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.356 -width 0 -relwidth 0.807 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab50 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.422 -width 0 -relwidth 0.823 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.489 -width 0 -relwidth 0.823 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.556 -width 0 -relwidth 0.823 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.622 -width 0 -relwidth 0.873 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -relx 0.679 -y 0 -rely 0.933 -width 0 -relwidth 0.311 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $top.but55 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.733 -width 567 -relwidth 0 \
        -height 84 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

