"""
File: my_drawing.py
Name: Amber Chang
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    I draw my favorite NBA player, Stephen Curry, to celebrate
    his second winning in the 3-Point Contest. In addition, I am
    extremely happy to see Curry playing on the court again after
    last year's injury.
    """
    window = GWindow(600, 800, title='Stephen Curry')

    # Background
    background = GRect(window.width, window.height)
    background.filled = True
    background.fill_color = 'royalblue'
    background.color = 'royalblue'
    window.add(background)

    # Title
    label = GLabel('STEPHEN CURRY')
    label.color = 'gold'
    label.font = 'Times New Roman-50-bold'
    window.add(label, (window.width - label.width) / 2, 100)

    # Floor
    floor = GRect(window.width, 130)
    floor.filled = True
    floor.fill_color = 'moccasin'
    floor.color = 'wheat'
    window.add(floor, 0, 670)

    # Stephen Curry
    # Shadow
    c_shadow = GOval(180, 20)
    c_shadow.filled = True
    c_shadow.fill_color = 'gray'
    c_shadow.color = 'gray'
    window.add(c_shadow, 251, 740)

    # Right Shoe
    right_shoe_bottom = GPolygon()
    right_shoe_bottom.add_vertex((320, 742))
    right_shoe_bottom.add_vertex((320, 747))
    right_shoe_bottom.add_vertex((370, 730))
    right_shoe_bottom.add_vertex((378, 728))
    right_shoe_bottom.add_vertex((380, 720))
    right_shoe_bottom.add_vertex((376, 715))
    right_shoe_bottom.filled = True
    right_shoe_bottom.fill_color = 'snow'
    right_shoe_bottom.color = 'navy'
    window.add(right_shoe_bottom)

    right_shoe_head = GOval(21, 13)
    right_shoe_head.filled = True
    right_shoe_head.fill_color = 'snow'
    right_shoe_head.color = 'navy'
    window.add(right_shoe_head, 305, 735)

    right_shoe = GPolygon()
    right_shoe.add_vertex((338, 700))
    right_shoe.add_vertex((340, 715))
    right_shoe.add_vertex((313, 735))
    right_shoe.add_vertex((310, 743))
    right_shoe.add_vertex((320, 746))
    right_shoe.add_vertex((365, 725))
    right_shoe.add_vertex((376, 715))
    right_shoe.add_vertex((362, 693))
    right_shoe.filled = True
    right_shoe.fill_color = 'snow'
    right_shoe.color = 'snow'
    window.add(right_shoe)

    shoelace1 = GPolygon()
    shoelace1.add_vertex((330, 723))
    shoelace1.add_vertex((340, 717))
    shoelace1.add_vertex((340, 709))
    shoelace1.add_vertex((337, 717))
    shoelace1.filled = True
    shoelace1.fill_color = 'navy'
    shoelace1.color = 'navy'
    window.add(shoelace1)

    r_shoe_line1 = GLine(x0=327, x1=328, y0=733, y1=737)
    r_shoe_line1.color = 'navy'
    window.add(r_shoe_line1)

    r_shoe_line2 = GLine(x0=330, x1=334, y0=730, y1=735)
    r_shoe_line2.color = 'navy'
    window.add(r_shoe_line2)

    r_shoe_detail1 = GLine(x0=307, x1=321, y0=746, y1=743)
    r_shoe_detail1.color = 'navy'
    window.add(r_shoe_detail1)

    r_shoe_detail2 = GLine(x0=321, x1=379, y0=743, y1=719)
    r_shoe_detail2.color = 'navy'
    window.add(r_shoe_detail2)

    r_shoe_detail3 = GPolygon()
    r_shoe_detail3.add_vertex((353, 705))
    r_shoe_detail3.add_vertex((355, 708))
    r_shoe_detail3.add_vertex((357, 716))
    r_shoe_detail3.filled = True
    r_shoe_detail3.fill_color = 'navy'
    r_shoe_detail3.color = 'navy'
    window.add(r_shoe_detail3)

    r_shoe_detail4 = GPolygon()
    r_shoe_detail4.add_vertex((356, 701))
    r_shoe_detail4.add_vertex((358, 704))
    r_shoe_detail4.add_vertex((359, 710))
    r_shoe_detail4.filled = True
    r_shoe_detail4.fill_color = 'navy'
    r_shoe_detail4.color = 'navy'
    window.add(r_shoe_detail4)

    r_shoe_detail5 = GLine(x0=315, x1=338, y0=744, y1=732)
    r_shoe_detail5.color = 'navy'
    window.add(r_shoe_detail5)

    r_shoe_detail6 = GLine(x0=338, x1=361, y0=732, y1=718)
    r_shoe_detail6.color = 'navy'
    window.add(r_shoe_detail6)

    r_shoe_detail7 = GLine(x0=361, x1=374, y0=718, y1=714)
    r_shoe_detail7.color = 'navy'
    window.add(r_shoe_detail7)

    r_outline1 = GLine(x0=338, x1=340, y0=700, y1=715)
    r_outline1.color = 'navy'
    window.add(r_outline1)

    r_outline2 = GLine(x0=340, x1=313, y0=715, y1=735)
    r_outline2.color = 'navy'
    window.add(r_outline2)

    r_outline3 = GLine(x0=376, x1=362, y0=716, y1=693)
    r_outline3.color = 'navy'
    window.add(r_outline3)

    # Right Leg
    right_ankle = GPolygon()
    right_ankle.add_vertex((338, 700))
    right_ankle.add_vertex((362, 693))
    right_ankle.add_vertex((353, 680))
    right_ankle.add_vertex((344, 662))
    right_ankle.add_vertex((321, 672))
    right_ankle.add_vertex((335, 688))
    right_ankle.filled = True
    right_ankle.fill_color = 'snow'
    right_ankle.color = 'navy'
    window.add(right_ankle)

    r_sock1 = GLine(x0=327, x1=333, y0=674, y1=681)
    r_sock1.color = 'navy'
    window.add(r_sock1)

    r_sock2 = GLine(x0=330, x1=335, y0=673, y1=679)
    r_sock2.color = 'navy'
    window.add(r_sock2)

    r_sock3 = GLine(x0=333, x1=340, y0=672, y1=680)
    r_sock3.color = 'navy'
    window.add(r_sock3)

    r_protect = GPolygon()
    r_protect.add_vertex((337, 701))
    r_protect.add_vertex((335, 693))
    r_protect.add_vertex((338, 686))
    r_protect.add_vertex((355, 680))
    r_protect.add_vertex((362, 692))
    r_protect.filled = True
    r_protect.fill_color = 'snow'
    r_protect.color = 'navy'
    window.add(r_protect)

    right_calf = GPolygon()
    right_calf.add_vertex((322, 672))
    right_calf.add_vertex((343, 662))
    right_calf.add_vertex((338, 648))
    right_calf.add_vertex((313, 660))
    right_calf.filled = True
    right_calf.fill_color = 'peru'
    right_calf.color = 'navy'
    window.add(right_calf)

    right_thigh = GPolygon()
    right_thigh.add_vertex((280, 596))
    right_thigh.add_vertex((275, 615))
    right_thigh.add_vertex((300, 610))
    right_thigh.add_vertex((313, 610))
    right_thigh.add_vertex((313, 598))
    right_thigh.filled = True
    right_thigh.fill_color = 'navy'
    right_thigh.color = 'navy'
    window.add(right_thigh)

    right_knee = GPolygon()
    right_knee.add_vertex((275, 615))
    right_knee.add_vertex((273, 625))
    right_knee.add_vertex((275, 630))
    right_knee.add_vertex((287, 643))
    right_knee.add_vertex((297, 645))
    right_knee.add_vertex((313, 660))
    right_knee.add_vertex((338, 648))
    right_knee.add_vertex((334, 640))
    right_knee.add_vertex((314, 618))
    right_knee.add_vertex((313, 611))
    right_knee.add_vertex((300, 610))
    right_knee.filled = True
    right_knee.fill_color = 'snow'
    right_knee.color = 'navy'
    window.add(right_knee)

    r_knee_line1 = GPolygon()
    r_knee_line1.add_vertex((290, 629))
    r_knee_line1.add_vertex((297, 627))
    r_knee_line1.add_vertex((308, 621))
    r_knee_line1.filled = True
    r_knee_line1.fill_color = 'navy'
    r_knee_line1.color = 'navy'
    window.add(r_knee_line1)

    r_knee_line2 = GPolygon()
    r_knee_line2.add_vertex((294, 623))
    r_knee_line2.add_vertex((302, 621))
    r_knee_line2.add_vertex((306, 619))
    r_knee_line2.filled = True
    r_knee_line2.fill_color = 'navy'
    r_knee_line2.color = 'navy'
    window.add(r_knee_line2)

    r_knee_line3 = GPolygon()
    r_knee_line3.add_vertex((299, 632))
    r_knee_line3.add_vertex((308, 627))
    r_knee_line3.add_vertex((309, 625))
    r_knee_line3.filled = True
    r_knee_line3.fill_color = 'navy'
    r_knee_line3.color = 'navy'
    window.add(r_knee_line3)

    r_knee_line4 = GPolygon()
    r_knee_line4.add_vertex((316, 654))
    r_knee_line4.add_vertex((322, 650))
    r_knee_line4.add_vertex((330, 647))
    r_knee_line4.filled = True
    r_knee_line4.fill_color = 'navy'
    r_knee_line4.color = 'navy'
    window.add(r_knee_line4)

    # Left Shoe
    left_shoe_head = GOval(28, 15)
    left_shoe_head.filled = True
    left_shoe_head.fill_color = 'snow'
    left_shoe_head.color = 'navy'
    window.add(left_shoe_head, 176, 737)

    left_shoe = GPolygon()
    left_shoe.add_vertex((195, 752))
    left_shoe.add_vertex((253, 752))
    left_shoe.add_vertex((261, 750))
    left_shoe.add_vertex((256, 730))
    left_shoe.add_vertex((258, 715))
    left_shoe.add_vertex((236, 716))
    left_shoe.add_vertex((233, 712))
    left_shoe.add_vertex((217, 727))
    left_shoe.add_vertex((185, 738))
    left_shoe.add_vertex((180, 745))
    left_shoe.filled = True
    left_shoe.fill_color = 'snow'
    left_shoe.color = 'snow'
    window.add(left_shoe)

    shoelace = GPolygon()
    shoelace.add_vertex((205, 733))
    shoelace.add_vertex((209, 738))
    shoelace.add_vertex((209, 732))
    shoelace.add_vertex((216, 736))
    shoelace.add_vertex((215, 728))
    shoelace.add_vertex((223, 732))
    shoelace.add_vertex((222, 723))
    shoelace.add_vertex((230, 730))
    shoelace.add_vertex((225, 719))
    shoelace.add_vertex((233, 721))
    shoelace.add_vertex((230, 717))
    shoelace.filled = True
    shoelace.fill_color = 'snow'
    shoelace.color = 'navy'
    window.add(shoelace)

    l_shoe_line1 = GPolygon()
    l_shoe_line1.add_vertex((247, 720))
    l_shoe_line1.add_vertex((243, 727))
    l_shoe_line1.add_vertex((245, 725))
    l_shoe_line1.filled = True
    l_shoe_line1.fill_color = 'navy'
    l_shoe_line1.color = 'navy'
    window.add(l_shoe_line1)

    l_shoe_line2 = GLine(x0=251, x1=250, y0=720, y1=724)
    l_shoe_line2.color = 'navy'
    window.add(l_shoe_line2)

    l_shoe_detail1 = GLine(x0=233, x1=230, y0=718, y1=730)
    l_shoe_detail1.color = 'navy'
    window.add(l_shoe_detail1)

    l_shoe_detail2 = GLine(x0=231, x1=205, y0=730, y1=739)
    l_shoe_detail2.color = 'navy'
    window.add(l_shoe_detail2)

    l_shoe_detail3 = GLine(x0=176, x1=191, y0=745, y1=749)
    l_shoe_detail3.color = 'navy'
    window.add(l_shoe_detail3)

    l_shoe_detail4 = GLine(x0=191, x1=259, y0=749, y1=745)
    l_shoe_detail4.color = 'navy'
    window.add(l_shoe_detail4)

    l_shoe_detail5 = GLine(x0=185, x1=191, y0=747, y1=744)
    l_shoe_detail5.color = 'navy'
    window.add(l_shoe_detail5)

    l_shoe_detail6 = GLine(x0=191, x1=202, y0=744, y1=745)
    l_shoe_detail6.color = 'navy'
    window.add(l_shoe_detail6)

    l_shoe_detail7 = GLine(x0=202, x1=243, y0=745, y1=736)
    l_shoe_detail7.color = 'navy'
    window.add(l_shoe_detail7)

    l_shoe_detail8 = GLine(x0=243, x1=258, y0=736, y1=738)
    l_shoe_detail8.color = 'navy'
    window.add(l_shoe_detail8)

    l_outline1 = GLine(x0=194, x1=250, y0=752, y1=752)
    l_outline1.color = 'navy'
    window.add(l_outline1)

    l_outline2 = GLine(x0=250, x1=261, y0=752, y1=750)
    l_outline2.color = 'navy'
    window.add(l_outline2)

    l_outline3 = GLine(x0=261, x1=256, y0=750, y1=730)
    l_outline3.color = 'navy'
    window.add(l_outline3)

    l_outline4 = GLine(x0=256, x1=258, y0=730, y1=715)
    l_outline4.color = 'navy'
    window.add(l_outline4)

    l_outline5 = GLine(x0=233, x1=217, y0=712, y1=727)
    l_outline5.color = 'navy'
    window.add(l_outline5)

    l_outline6 = GLine(x0=217, x1=184, y0=727, y1=738)
    l_outline6.color = 'navy'
    window.add(l_outline6)

    # Left Leg
    left_ankle = GPolygon()
    left_ankle.add_vertex((233, 712))
    left_ankle.add_vertex((236, 716))
    left_ankle.add_vertex((258, 715))
    left_ankle.add_vertex((260, 697))
    left_ankle.add_vertex((264, 679))
    left_ankle.add_vertex((237, 677))
    left_ankle.add_vertex((237, 697))
    left_ankle.filled = True
    left_ankle.fill_color = 'snow'
    left_ankle.color = 'navy'
    window.add(left_ankle)

    l_protect = GPolygon()
    l_protect.add_vertex((233, 712))
    l_protect.add_vertex((234, 698))
    l_protect.add_vertex((244, 699))
    l_protect.add_vertex((261, 702))
    l_protect.add_vertex((260, 713))
    l_protect.add_vertex((243, 716))
    l_protect.filled = True
    l_protect.fill_color = 'snow'
    l_protect.color = 'navy'
    window.add(l_protect)

    l_sock1 = GLine(x0=252, x1=252, y0=687, y1=695)
    l_sock1.color = 'navy'
    window.add(l_sock1)

    l_sock2 = GLine(x0=255, x1=254, y0=685, y1=695)
    l_sock2.color = 'navy'
    window.add(l_sock2)

    l_sock3 = GLine(x0=259, x1=257, y0=683, y1=695)
    l_sock3.color = 'navy'
    window.add(l_sock3)

    left_calf1 = GPolygon()
    left_calf1.add_vertex((238, 677))
    left_calf1.add_vertex((263, 679))
    left_calf1.add_vertex((267, 662))
    left_calf1.add_vertex((236, 660))
    left_calf1.filled = True
    left_calf1.fill_color = 'peru'
    left_calf1.color = 'navy'
    window.add(left_calf1)

    lef_calf2 = GPolygon()
    lef_calf2.add_vertex((235, 660))
    lef_calf2.add_vertex((268, 662))
    lef_calf2.add_vertex((269, 650))
    lef_calf2.add_vertex((268, 620))
    lef_calf2.add_vertex((272, 613))
    lef_calf2.add_vertex((233, 608))
    lef_calf2.add_vertex((232, 620))
    lef_calf2.add_vertex((237, 640))
    lef_calf2.filled = True
    lef_calf2.fill_color = 'snow'
    lef_calf2.color = 'navy'
    window.add(lef_calf2)

    l_knee_line1 = GPolygon()
    l_knee_line1.add_vertex((242, 615))
    l_knee_line1.add_vertex((250, 617))
    l_knee_line1.add_vertex((261, 618))
    l_knee_line1.filled = True
    l_knee_line1.fill_color = 'navy'
    l_knee_line1.color = 'navy'
    window.add(l_knee_line1)

    l_knee_line2 = GPolygon()
    l_knee_line2.add_vertex((245, 621))
    l_knee_line2.add_vertex((248, 622))
    l_knee_line2.add_vertex((260, 622))
    l_knee_line2.filled = True
    l_knee_line2.fill_color = 'navy'
    l_knee_line2.color = 'navy'
    window.add(l_knee_line2)

    l_knee_line3 = GPolygon()
    l_knee_line3.add_vertex((249, 626))
    l_knee_line3.add_vertex((252, 627))
    l_knee_line3.add_vertex((259, 626))
    l_knee_line3.filled = True
    l_knee_line3.fill_color = 'navy'
    l_knee_line3.color = 'navy'
    window.add(l_knee_line3)

    l_knee_line4 = GPolygon()
    l_knee_line4.add_vertex((243, 656))
    l_knee_line4.add_vertex((249, 657))
    l_knee_line4.add_vertex((263, 658))
    l_knee_line4.filled = True
    l_knee_line4.fill_color = 'navy'
    l_knee_line4.color = 'navy'
    window.add(l_knee_line4)

    left_thigh = GPolygon()
    left_thigh.add_vertex((233, 608))
    left_thigh.add_vertex((272, 613))
    left_thigh.add_vertex((277, 598))
    left_thigh.add_vertex((237, 593))
    left_thigh.filled = True
    left_thigh.fill_color = 'navy'
    left_thigh.color = 'navy'
    window.add(left_thigh)

    # Shorts
    shorts = GPolygon()
    shorts.add_vertex((227, 590))
    shorts.add_vertex((290, 598))
    shorts.add_vertex((291, 596))
    shorts.add_vertex((322, 596))
    shorts.add_vertex((321, 560))
    shorts.add_vertex((324, 540))
    shorts.add_vertex((330, 520))
    shorts.add_vertex((328, 475))
    shorts.add_vertex((252, 478))
    shorts.add_vertex((240, 515))
    shorts.add_vertex((230, 580))
    shorts.filled = True
    shorts.fill_color = 'snow'
    shorts.color = 'navy'
    window.add(shorts)

    line_1 = GPolygon()
    line_1.add_vertex((252, 505))
    line_1.add_vertex((259, 485))
    line_1.add_vertex((255, 495))
    line_1.filled = True
    line_1.fill_color = 'navy'
    line_1.color = 'navy'
    window.add(line_1)

    line_2 = GPolygon()
    line_2.add_vertex((263, 495))
    line_2.add_vertex((254, 525))
    line_2.add_vertex((257, 513))
    line_2.filled = True
    line_2.fill_color = 'navy'
    line_2.color = 'navy'
    window.add(line_2)

    line_3 = GPolygon()
    line_3.add_vertex((302, 485))
    line_3.add_vertex((294, 525))
    line_3.add_vertex((299, 504))
    line_3.filled = True
    line_3.fill_color = 'navy'
    line_3.color = 'navy'
    window.add(line_3)

    line_4 = GPolygon()
    line_4.add_vertex((307, 502))
    line_4.add_vertex((299, 538))
    line_4.add_vertex((304, 519))
    line_4.filled = True
    line_4.fill_color = 'navy'
    line_4.color = 'navy'
    window.add(line_4)

    stripe3 = GPolygon()
    stripe3.add_vertex((275, 478))
    stripe3.add_vertex((263, 530))
    stripe3.add_vertex((246, 592))
    stripe3.add_vertex((253, 593))
    stripe3.add_vertex((283, 478))
    stripe3.filled = True
    stripe3.fill_color = 'gold'
    stripe3.color = 'navy'
    window.add(stripe3)
    stripe4 = GPolygon()
    stripe4.add_vertex((289, 478))
    stripe4.add_vertex((260, 593))
    stripe4.add_vertex((267, 595))
    stripe4.add_vertex((295, 478))
    stripe4.filled = True
    stripe4.fill_color = 'gold'
    stripe4.color = 'navy'
    window.add(stripe4)

    pattern1 = GPolygon()
    pattern1.add_vertex((227, 590))
    pattern1.add_vertex((290, 598))
    pattern1.add_vertex((293, 590))
    pattern1.add_vertex((286, 565))
    pattern1.add_vertex((283, 550))
    pattern1.add_vertex((282, 537))
    pattern1.add_vertex((270, 587))
    pattern1.add_vertex((248, 583))
    pattern1.add_vertex((262, 533))
    pattern1.add_vertex((246, 555))
    pattern1.add_vertex((232, 570))
    pattern1.filled = True
    pattern1.fill_color = 'navy'
    pattern1.color = 'navy'
    window.add(pattern1)
    pattern2 = GPolygon()
    pattern2.add_vertex((292, 596))
    pattern2.add_vertex((322, 596))
    pattern2.add_vertex((321, 589))
    pattern2.add_vertex((295, 590))
    pattern2.filled = True
    pattern2.fill_color = 'navy'
    pattern2.color = 'navy'
    window.add(pattern2)

    shorts_line = GPolygon()
    shorts_line.add_vertex((291, 596))
    shorts_line.add_vertex((310, 525))
    shorts_line.add_vertex((307, 540))
    shorts_line.filled = True
    shorts_line.fill_color = 'navy'
    shorts_line.color = 'navy'
    window.add(shorts_line)

    # Right Arm
    right_arm = GPolygon()
    right_arm.add_vertex((272, 344))
    right_arm.add_vertex((237, 257))
    right_arm.add_vertex((232, 250))
    right_arm.add_vertex((215, 247))
    right_arm.add_vertex((208, 241))
    right_arm.add_vertex((208, 230))
    right_arm.add_vertex((217, 228))
    right_arm.add_vertex((203, 207))
    right_arm.add_vertex((206, 204))
    right_arm.add_vertex((223, 222))
    right_arm.add_vertex((213, 198))
    right_arm.add_vertex((216, 196))
    right_arm.add_vertex((230, 218))
    right_arm.add_vertex((223, 201))
    right_arm.add_vertex((226, 199))
    right_arm.add_vertex((245, 237))
    right_arm.add_vertex((251, 245))
    right_arm.add_vertex((300, 339))
    right_arm.filled = True
    right_arm.fill_color = 'peru'
    right_arm.color = 'navy'
    window.add(right_arm)

    right_hand = GOval(7, 6)
    right_hand.filled = True
    right_hand.fill_color = 'royalblue'
    right_hand.color = 'navy'
    window.add(right_hand, 213, 234)

    # Face
    face = GPolygon()
    face.add_vertex((283, 345))
    face.add_vertex((322, 350))
    face.add_vertex((305, 307))
    face.add_vertex((306, 290))
    face.add_vertex((270, 277))
    face.add_vertex((255, 278))
    face.add_vertex((253, 288))
    face.add_vertex((255, 298))
    face.add_vertex((251, 309))
    face.add_vertex((251, 311))
    face.add_vertex((253, 311))
    face.add_vertex((254, 316))
    face.add_vertex((260, 319))
    face.add_vertex((258, 323))
    face.add_vertex((262, 329))
    face.add_vertex((275, 326))
    face.filled = True
    face.fill_color = 'peru'
    face.color = 'navy'
    window.add(face)

    ear1 = GOval(10, 15)
    ear1.filled = True
    ear1.fill_color = 'peru'
    ear1.color = 'navy'
    window.add(ear1, 278, 288)
    ear2 = GOval(6, 10)
    ear2.filled = True
    ear2.fill_color = 'peru'
    ear2.color = 'peru'
    window.add(ear2, 277, 293)

    jaw_line1 = GLine(x0=283, x1=285, y0=303, y1=312)
    jaw_line1.color = 'navy'
    window.add(jaw_line1)
    jaw_line2 = GLine(x0=285, x1=277, y0=311, y1=320)
    jaw_line2.color = 'navy'
    window.add(jaw_line2)

    eyebrow = GLine(x0=254, x1=259, y0=296, y1=293)
    eyebrow.color = 'navy'
    window.add(eyebrow)

    beard = GPolygon()
    beard.add_vertex((259, 323))
    beard.add_vertex((260, 332))
    beard.add_vertex((263, 334))
    beard.add_vertex((270, 331))
    beard.add_vertex((272, 319))
    beard.add_vertex((262, 324))
    beard.filled = True
    beard.fill_color = 'navy'
    beard.color = 'navy'
    window.add(beard)

    # Hair
    hair = GPolygon()
    hair.add_vertex((255, 278))
    hair.add_vertex((270, 277))
    hair.add_vertex((306, 290))
    hair.add_vertex((308, 280))
    hair.add_vertex((306, 270))
    hair.add_vertex((300, 262))
    hair.add_vertex((287, 256))
    hair.add_vertex((270, 260))
    hair.add_vertex((265, 263))
    hair.add_vertex((256, 270))
    hair.filled = True
    hair.fill_color = 'navy'
    hair.color = 'navy'
    window.add(hair)

    # Jersey
    jersey = GPolygon()
    jersey.add_vertex((252, 478))
    jersey.add_vertex((331, 476))
    jersey.add_vertex((334, 392))
    jersey.add_vertex((325, 339))
    jersey.add_vertex((303, 333))
    jersey.add_vertex((272, 350))
    jersey.add_vertex((277, 334))
    jersey.add_vertex((261, 365))
    jersey.add_vertex((251, 465))
    jersey.filled = True
    jersey.fill_color = 'snow'
    jersey.color = 'navy'
    window.add(jersey)

    line1 = GPolygon()
    line1.add_vertex((286, 410))
    line1.add_vertex((269, 423))
    line1.add_vertex((277, 416))
    line1.filled = True
    line1.fill_color = 'navy'
    line1.color = 'navy'
    window.add(line1)

    line2 = GPolygon()
    line2.add_vertex((278, 426))
    line2.add_vertex((262, 439))
    line2.add_vertex((268, 433))
    line2.filled = True
    line2.fill_color = 'navy'
    line2.color = 'navy'
    window.add(line2)

    line3 = GPolygon()
    line3.add_vertex((270, 443))
    line3.add_vertex((257, 457))
    line3.add_vertex((262, 450))
    line3.filled = True
    line3.fill_color = 'navy'
    line3.color = 'navy'
    window.add(line3)

    collar = GPolygon()
    collar.add_vertex((277, 334))
    collar.add_vertex((272, 350))
    collar.add_vertex((303, 333))
    collar.add_vertex((325, 339))
    collar.add_vertex((325, 335))
    collar.add_vertex((305, 331))
    collar.add_vertex((276, 343))
    collar.filled = True
    collar.fill_color = 'navy'
    collar.color = 'navy'
    window.add(collar)

    stripe1 = GPolygon()
    stripe1.add_vertex((289, 400))
    stripe1.add_vertex((289, 440))
    stripe1.add_vertex((280, 477))
    stripe1.add_vertex((288, 477))
    stripe1.add_vertex((296, 440))
    stripe1.add_vertex((296, 400))
    stripe1.filled = True
    stripe1.fill_color = 'gold'
    stripe1.color = 'navy'
    window.add(stripe1)
    stripe2 = GPolygon()
    stripe2.add_vertex((302, 410))
    stripe2.add_vertex((302, 440))
    stripe2.add_vertex((296, 477))
    stripe2.add_vertex((304, 477))
    stripe2.add_vertex((309, 410))
    stripe2.filled = True
    stripe2.fill_color = 'gold'
    stripe2.color = 'navy'
    window.add(stripe2)

    sleeveless1 = GOval(55, 65)
    sleeveless1.filled = True
    sleeveless1.fill_color = 'navy'
    sleeveless1.color = 'navy'
    window.add(sleeveless1, 276, 340)

    sleeveless2 = GPolygon()
    sleeveless2.add_vertex((261, 365))
    sleeveless2.add_vertex((277, 334))
    sleeveless2.add_vertex((261, 363))
    sleeveless2.filled = True
    sleeveless2.fill_color = 'navy'
    sleeveless2.color = 'navy'
    window.add(sleeveless2)

    # Left Arm
    upper_arm = GOval(50, 58)
    upper_arm.filled = True
    upper_arm.fill_color = 'peru'
    upper_arm.color = 'navy'
    window.add(upper_arm, 279, 343)

    arm = GPolygon()
    arm.add_vertex((295, 380))
    arm.add_vertex((301, 410))
    arm.add_vertex((311, 440))
    arm.add_vertex((315, 460))
    arm.add_vertex((320, 478))
    arm.add_vertex((330, 520))
    arm.add_vertex((350, 518))
    arm.add_vertex((345, 496))
    arm.add_vertex((342, 476))
    arm.add_vertex((340, 435))
    arm.add_vertex((334, 405))
    arm.add_vertex((328, 385))
    arm.filled = True
    arm.fill_color = 'peru'
    arm.color = 'navy'
    window.add(arm)

    arm_line = GRect(31, 7)
    arm_line.filled = True
    arm_line.fill_color = 'peru'
    arm_line.color = 'peru'
    window.add(arm_line, 295, 380)

    wrist = GPolygon()
    wrist.add_vertex((329, 520))
    wrist.add_vertex((351, 518))
    wrist.add_vertex((351, 522))
    wrist.add_vertex((330, 524))
    wrist.filled = True
    wrist.fill_color = 'navy'
    wrist.color = 'navy'
    window.add(wrist)

    arm_pit = GPolygon()
    arm_pit.add_vertex((295, 385))
    arm_pit.add_vertex((290, 380))
    arm_pit.add_vertex((297, 394))
    arm_pit.filled = True
    arm_pit.fill_color = 'navy'
    arm_pit.color = 'navy'
    window.add(arm_pit)

    # Left Hand
    left_hand = GPolygon()
    left_hand.add_vertex((330, 524))
    left_hand.add_vertex((351, 522))
    left_hand.add_vertex((358, 536))
    left_hand.add_vertex((361, 554))
    left_hand.add_vertex((359, 556))
    left_hand.add_vertex((354, 537))
    left_hand.add_vertex((358, 563))
    left_hand.add_vertex((354, 565))
    left_hand.add_vertex((348, 540))
    left_hand.add_vertex((352, 567))
    left_hand.add_vertex((347, 567))
    left_hand.add_vertex((342, 540))
    left_hand.add_vertex((345, 566))
    left_hand.add_vertex((340, 565))
    left_hand.add_vertex((335, 541))
    left_hand.add_vertex((337, 560))
    left_hand.add_vertex((332, 556))
    left_hand.add_vertex((328, 536))
    left_hand.filled = True
    left_hand.fill_color = 'peru'
    left_hand.color = 'navy'
    window.add(left_hand)

    # Basketball shadow
    shadow = GOval(70, 20)
    shadow.filled = True
    shadow.fill_color = 'gray'
    shadow.color = 'gray'
    window.add(shadow, 478, 683)

    # Basketball
    ball = GOval(80, 80)
    ball.filled = True
    ball.fill_color = 'darkorange'
    window.add(ball, 450, 620)
    line1 = GOval(80, 60)
    line1.filled = True
    line1.fill_color = 'darkorange'
    window.add(line1, 450, 630)
    line2 = GLine(x0=450, x1=530, y0=660, y1=660)
    window.add(line2)

    # Brand Name 'SPALDING'
    brand1 = GLabel('S')
    brand1.font = 'Impact-17'
    window.add(brand1, 461, 661)
    brand2 = GLabel('P')
    brand2.font = 'Impact-15'
    window.add(brand2, 470, 658)
    brand3 = GLabel('A')
    brand3.font = 'Impact-13'
    window.add(brand3, 478, 656)
    brand4 = GLabel('L')
    brand4.font = 'Impact-13'
    window.add(brand4, 486, 656)
    brand5 = GLabel('D')
    brand5.font = 'Impact-13'
    window.add(brand5, 492, 656)
    brand6 = GLabel('I')
    brand6.font = 'Impact-13'
    window.add(brand6, 500, 656)
    brand7 = GLabel('N')
    brand7.font = 'Impact-15'
    window.add(brand7, 504, 658)
    brand8 = GLabel('G')
    brand8.font = 'Impact-17'
    window.add(brand8, 512, 661)

    # Logo
    logo1 = GOval(10, 7)
    logo1.filled = True
    logo1.fill_color = 'darkorange'
    window.add(logo1, 485, 633)
    logo2 = GLabel('S')
    logo2.font = 'Courier-7-italic'
    window.add(logo2, 488, 641)

    # NBA Logo
    frame = GRect(10, 20)
    frame.filled = True
    frame.fill_color = 'black'
    window.add(frame, 485, 664)
    nba = GLabel('NBA')
    nba.color = 'white'
    nba.font = 'Times-3-bold'
    window.add(nba, 485, 685)
    head = GOval(2, 3)
    head.filled = True
    head.fill_color = 'darkorange'
    head.color = 'darkorange'
    window.add(head, 490, 664)
    body = GPolygon()
    body.add_vertex((490, 667))
    body.add_vertex((484, 673))
    body.add_vertex((493, 685))
    body.filled = True
    body.fill_color = 'darkorange'
    body.color = 'darkorange'
    window.add(body)
    small_ball = GOval(3, 3)
    small_ball.filled = True
    small_ball.color = 'darkorange'
    small_ball.fill_color = 'darkorange'
    window.add(small_ball, 493, 674)
    arm = GLine(x0=490, x1=494, y0=667, y1=674)
    arm.color = 'darkorange'
    window.add(arm)

    # Words on the Basketball
    word1 = GLabel('GAME BALL SERIES')
    word1.font = '-2-bold'
    window.add(word1, 462, 672)
    word2 = GLabel('OUTDOOR')
    word2.font = '-1'
    window.add(word2, 470, 674)
    word3 = GLabel('Adam Silver')
    word3.font = 'Apple Chancery-4'
    window.add(word3, 498, 674)
    word4 = GLabel('COMMISSIONER')
    word4.font = '-1'
    window.add(word4, 504, 674)


if __name__ == '__main__':
    main()
