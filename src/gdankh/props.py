TYPES = {
    "1": "int",   # id
    "2": "float",   # x
    "3": "float",   # y
    "4": "bool",   # flip_horiz
    "5": "bool",   # flip_vert
    "6": "float",   # rotation
    "7": "int",   # red
    "8": "int",   # green
    "9": "int",   # blue
    "10": "float",   # duration
    "11": "bool",   # touch_triggered
    "12": "int",   # coin_id
    "13": "bool",   # preview
    "14": "bool",   # tint_ground
    "15": "bool",   # player_color_1
    "16": "bool",   # player_color_2
    "17": "bool",   # blending
    "19": "color1p9",   # color_1point9
    "20": "int",   # editor_layer
    "21": "int",   # color_1
    "22": "int",   # color_2
    "23": "colorid",   # target_color
    "24": "int",   # z_layer
    "25": "int",   # z_order
    "28": "int",   # move_x
    "29": "int",   # offset
    "30": "easing",   # easing
    "31": "string",   # text
    "32": "float",   # scale
    "33": "int",   # single_group
    "34": "bool",   # group_parent
    "35": "float",   # opacity
    "36": "bool",   # interactible
    "41": "bool",   # color_1_hsv_enabled
    "42": "bool",   # color_2_hsv_enabled
    "43": "hsvstring",   # color_1_hsv
    "44": "hsvstring",   # color_2_hsv
    "45": "float",   # fade_in
    "46": "float",   # hold
    "47": "float",   # fade_out
    "48": "bool",   # hsv_enabled
    "49": "hsvstring",   # hsv
    "50": "colorid",   # copy_color_id
    "51": "groupid",   # group_id
    "52": "bool",   # target_type
    "54": "float",   # orange_tp_portal_distance
    "55": "bool",   # smooth_ease
    "56": "bool",   # enable_group
    "57": "grouplist",   # groups
    "58": "bool",   # lock_x_player
    "59": "bool",   # lock_y_player
    "60": "bool",   # copy_opacity
    "61": "int",   # editor_layer_2
    "62": "bool",   # spawn_triggered
    "63": "float",   # delay
    "64": "bool",   # dont_fade
    "65": "bool",   # main_only
    "66": "bool",   # detail_only
    "67": "bool",   # dont_enter
    "68": "float",   # degrees
    "69": "int",   # x360
    "70": "bool",   # lock_obj_rot
    "71": "groupid",   # spawn_gid
    "72": "float",   # x_mod
    "73": "float",   # y_mod
    "75": "float",   # strength
    "76": "int",   # animation_id
    "77": "int",   # target_count
    "78": "bool",   # sub_count
    "80": "itemid",   # item_id
    "81": "bool",   # hold_mode
    "82": "touchtoggle",   # toggle_on_off
    "84": "float",   # interval
    "85": "float",   # easing_rate
    "86": "bool",   # exclusive
    "87": "bool",   # multi_triggered
    "88": "instantcountcomparison",   # comparison
    "89": "bool",   # dual_mode
    "90": "float",   # speed
    "91": "float",   # delay
    "92": "int",   # offset
    "93": "bool",   # trigger_on_exit
    "94": "bool",   # dynamic_block
    "95": "itemortimerid",   # item_id_2
    "96": "bool",   # no_glow
    "97": "float",   # rotation_speed
    "98": "bool",   # disable_rotation
    "99": "bool",   # multi_activate_classic
    "100": "bool",   # target_mode
    "101": "xyonly",   # mode_xy_only
    "102": "bool",   # preview_disable
    "103": "bool",   # high_detail
    "104": "bool",   # multi_activate
    "105": "float",   # max_speed
    "106": "bool",   # randomize_start
    "107": "float",   # speed
    "108": "int",   # linked_group
    "110": "bool",   # exit_static
    "111": "bool",   # free_mode
    "112": "bool",   # edit_camera_settings
    "113": "int",   # camera_easing
    "114": "float",   # padding
    "115": "int",   # ord
    "116": "bool",   # no_effects
    "117": "bool",   # reverse
    "118": "bool",   # reversed
    "120": "float",   # time_mod
    "121": "bool",   # no_touch
    "122": "bool",   # use_speed
    "123": "bool",   # animate_on_trigger
    "126": "bool",   # disable_delayed_loop
    "127": "bool",   # disable_animshine
    "128": "float",   # scale_x
    "129": "float",   # scale_y
    "131": "float",   # warp_y_angle
    "132": "float",   # warp_x_angle
    "133": "bool",   # only_move
    "134": "bool",   # passable
    "135": "bool",   # hide
    "136": "bool",   # non_stick_x
    "137": "bool",   # ice_block
    "138": "bool",   # mode_target_p1
    "139": "bool",   # override
    "141": "bool",   # lock_x_camera
    "142": "bool",   # lock_y_camera
    "143": "float",   # mod_x
    "144": "float",   # mod_y
    "145": "particlestring",   # particle_data
    "146": "bool",   # use_obj_color
    "147": "bool",   # uniform_obj_color
    "148": "float",   # gravity
    "149": "float",   # force
    "150": "float",   # scale_trigger_scale_x
    "151": "float",   # scale_trigger_scale_y
    "152": "advrandomlist",   # list
    "153": "bool",   # div_x
    "154": "bool",   # div_y
    "155": "int",   # color_1_index
    "156": "int",   # color_2_index
    "157": "bool",   # reference_only
    "159": "optionset",   # streak_additive
    "160": "optionset",   # unlink_dual_gravity
    "161": "optionset",   # hide_ground
    "162": "optionset",   # hide_p1
    "163": "optionset",   # hide_p2
    "164": "cameraedge",   # edge
    "165": "optionset",   # disable_p1_controls
    "166": "arrowdir",   # gravity_dir
    "167": "arrowdir",   # arrow_dir
    "169": "bool",   # edit_velocity
    "170": "int",   # channel
    "171": "bool",   # change_channel
    "172": "bool",   # channel_only
    "173": "channelid",   # target_channel
    "174": "gradientblend",   # blending
    "175": "float",   # speed
    "176": "float",   # strength
    "177": "float",   # time_off
    "179": "float",   # wave_w
    "180": "float",   # thickness
    "181": "float",   # fade_in
    "182": "float",   # fade_out
    "183": "float",   # inner
    "184": "bool",   # invert
    "185": "bool",   # flip
    "186": "bool",   # rotate
    "187": "bool",   # dual
    "188": "bool",   # no_player_particles
    "189": "float",   # target_y
    "190": "bool",   # follow
    "191": "float",   # outer
    "192": "bool",   # disable_all
    "193": "bool",   # grip_slope
    "194": "bool",   # relative_pos
    "195": "optionset",   # hide_mg
    "196": "triggerlayer",   # lowest_layer
    "197": "triggerlayer",   # highest_layer
    "198": "touchplayeronly",   # p1_p2_only
    "199": "optionset",   # disable_p2_controls
    "200": "bool",   # mode_target_p2
    "201": "bool",   # follow_c
    "202": "triggerlayer",   # layer
    "203": "int",   # u_bl
    "204": "int",   # d_br
    "205": "int",   # l_tl
    "206": "int",   # r_tr
    "207": "bool",   # vertex_mode
    "208": "bool",   # disable
    "209": "int",   # gradient_id
    "210": "bool",   # legacy_hsv_off
    "211": "bool",   # quick_start
    "212": "bool",   # follow
    "213": "float",   # follow_easing
    "214": "bool",   # animate_active_only
    "217": "enterexitonly",   # enter_exit_only
    "218": "int",   # move_dist
    "219": "int",   # move_dist_pm
    "220": "int",   # offset
    "221": "int",   # offset_pm
    "222": "int",   # length
    "223": "int",   # length_pm
    "225": "effectid",   # effect_id
    "231": "int",   # move_angle
    "232": "int",   # move_angle_pm
    "233": "float",   # area_scale_x
    "234": "float",   # area_scale_x_pm
    "235": "float",   # area_scale_y
    "236": "float",   # area_scale_y_pm
    "237": "int",   # move_x
    "238": "int",   # move_x_pm
    "239": "int",   # move_y
    "240": "int",   # move_y_pm
    "241": "bool",   # xy_mode
    "242": "easing",   # area_easing
    "243": "float",   # area_easing_rate
    "248": "easing",   # area_easing2
    "249": "float",   # area_easing2_rate
    "252": "int",   # offset_y
    "253": "int",   # offset_y_pm
    "255": "bool",   # use_eid
    "260": "colorid",   # color_channel
    "261": "bool",   # ease_out
    "262": "areadirbuttonsdir",   # dir_buttons_dir
    "263": "float",   # mod_front
    "264": "float",   # mod_back
    "265": "float",   # tint
    "270": "float",   # area_rotation
    "271": "float",   # area_rotation_pm
    "274": "grouplist",   # parent_groups
    "275": "float",   # to_opacity
    "276": "bool",   # dir_buttons_inwards
    "278": "bool",   # hsv_on
    "279": "bool",   # area_parent
    "280": "bool",   # ignore_gparent
    "281": "bool",   # ignore_linked
    "282": "float",   # deadzone
    "283": "bool",   # dir_buttons_double_arrow
    "284": "bool",   # single_ptouch
    "285": "float",   # unknown
    "286": "float",   # from_opacity
    "287": "bool",   # relative
    "288": "float",   # rfade
    "289": "bool",   # non_stick_y
    "290": "float",   # screen_offx
    "291": "float",   # screen_offy
    "292": "float",   # delay
    "293": "float",   # delay_pm
    "298": "float",   # max_speed
    "299": "float",   # max_speed_pm
    "300": "float",   # start_speed
    "301": "float",   # start_speed_pm
    "305": "bool",   # target_dir
    "306": "bool",   # x_only
    "307": "bool",   # y_only
    "308": "int",   # max_range
    "309": "int",   # max_range_pm
    "316": "float",   # steer_force
    "317": "float",   # steer_force_pm
    "318": "float",   # steer_force_low
    "319": "float",   # steer_force_low_pm
    "320": "float",   # steer_force_high
    "321": "float",   # steer_force_high_pm
    "322": "float",   # speed_range_low
    "323": "float",   # speed_range_low_pm
    "324": "float",   # speed_range_high
    "325": "float",   # speed_range_high_pm
    "326": "float",   # break_force
    "327": "float",   # break_force_pm
    "328": "int",   # break_angle
    "329": "int",   # break_angle_pm
    "330": "float",   # break_steer_force
    "331": "float",   # break_steer_force_pm
    "332": "float",   # break_steer_speed_limit
    "333": "float",   # break_steer_speed_limit_pm
    "334": "float",   # acceleration
    "335": "float",   # acceleration_pm
    "336": "bool",   # ignore_disabled
    "337": "bool",   # steer_force_low_checkbox
    "338": "bool",   # steer_force_high_checkbox
    "339": "bool",   # rotate_dir
    "340": "int",   # rot_offset
    "341": "int",   # priority
    "343": "int",   # enter_channel
    "344": "int",   # target_enter_channel
    "345": "bool",   # static_force
    "346": "float",   # static_force_value
    "347": "bool",   # redirect_force
    "348": "float",   # redirect_force_min
    "349": "float",   # redirect_force_max
    "350": "float",   # redirect_force_mod
    "351": "bool",   # save_offset
    "352": "bool",   # ignore_x
    "353": "bool",   # ignore_y
    "354": "teleportgravity",   # exit_gravity
    "356": "bool",   # scale_stick
    "357": "float",   # near_accel
    "358": "float",   # near_accel_pm
    "359": "float",   # near_dist
    "360": "float",   # near_dist_pm
    "361": "float",   # follow_easing
    "362": "float",   # follow_easing_pm
    "363": "int",   # rot_easing
    "364": "int",   # rot_dead_z
    "365": "int",   # priority
    "366": "int",   # max_range_unmarked
    "367": "advancedfollowpage2mode",   # page_2_mode
    "368": "bool",   # instant_offset
    "369": "bool",   # center_effect
    "370": "bool",   # disable_gridsnap
    "371": "float",   # zoom
    "372": "bool",   # no_audio_scale
    "373": "int",   # anim_id
    "374": "int",   # order_index
    "375": "bool",   # ref_only
    "376": "bool",   # close_loop
    "377": "bool",   # prox
    "378": "bool",   # curve
    "379": "keyframemode",   # time_even_dist
    "380": "bool",   # preview_art
    "381": "bool",   # pickup_item
    "382": "bool",   # toggle_trigger
    "383": "int",   # points
    "385": "uiref",   # xref_pos
    "386": "uiref",   # yref_pos
    "387": "bool",   # xref_relative
    "388": "bool",   # yref_relative
    "389": "bool",   # seconds_only
    "390": "labelspecial",   # special
    "391": "labelalign",   # align
    "392": "int",   # song
    "393": "bool",   # small_step
    "394": "bool",   # direction_mode
    "395": "groupid",   # mode_center_group
    "396": "int",   # direction_mode_distance
    "397": "bool",   # dynamic_mode
    "399": "bool",   # prep
    "400": "bool",   # load_prep
    "401": "int",   # rot_target_id
    "402": "float",   # rot_offset
    "403": "int",   # dynamic_mode_easing
    "404": "int",   # speed
    "405": "int",   # pitch
    "406": "float",   # volume
    "407": "bool",   # reverb
    "408": "int",   # start
    "409": "int",   # fade_in
    "410": "int",   # end
    "411": "int",   # fade_out
    "412": "bool",   # fft
    "413": "bool",   # loop
    "414": "bool",   # stop_loop
    "415": "bool",   # is_unique
    "416": "uniqueid",   # unique_id
    "417": "bool",   # stop
    "418": "bool",   # change_volume
    "419": "bool",   # change_speed
    "420": "bool",   # override
    "421": "float",   # vol_near
    "422": "float",   # vol_med
    "423": "float",   # vol_far
    "424": "int",   # min_dist
    "425": "int",   # dist_2
    "426": "int",   # dist_3
    "428": "bool",   # cam
    "430": "eventlist",   # events
    "432": "int",   # song_channel
    "433": "bool",   # pre_load
    "434": "float",   # min_interval
    "435": "sequencelist",   # sequence
    "436": "sequencemode",   # mode
    "437": "float",   # min_int
    "438": "float",   # reset
    "439": "bool",   # reset_full_step
    "440": "int",   # particle
    "441": "bool",   # spawn_ordered
    "442": "remaplist",   # group_remaps
    "443": "bool",   # static_force_additive
    "444": "bool",   # no_multi_activate_platformer
    "445": "bool",   # claim_touch
    "446": "int",   # material
    "447": "int",   # extra_id
    "448": "groupid",   # respawn_id
    "449": "float",   # modifier
    "452": "bool",   # relative_rot
    "453": "bool",   # smooth_velocity
    "454": "float",   # smooth_velocity_modifier
    "455": "sfxgroup",   # sfx_group
    "456": "float",   # preview_opacity
    "457": "groupid",   # group_id
    "458": "sounddirs",   # dir_buttons
    "459": "bool",   # auto_layer
    "460": "bool",   # no_end_effects
    "461": "bool",   # no_sfx
    "462": "int",   # single_frame
    "463": "bool",   # no_anim
    "464": "bool",   # instant_camera
    "465": "bool",   # exit_instant
    "466": "bool",   # time_counter
    "467": "float",   # start_time
    "468": "bool",   # dont_override
    "469": "bool",   # ignore_timewarp
    "470": "float",   # time_mod
    "471": "bool",   # start_paused
    "472": "bool",   # start_stop
    "473": "float",   # stop_time
    "474": "bool",   # stop_checked
    "475": "bool",   # multi_activate
    "476": "itemtriggertyp",   # typ_1
    "477": "itemtriggertyp",   # typ_2
    "478": "itemtriggertyp",   # target_typ
    "479": "float",   # mod
    "480": "itemtriggerop",   # assign_op
    "481": "itemtriggerop",   # op_1
    "482": "itemtriggerop",   # op_2
    "483": "float",   # mod_2
    "484": "float",   # tol_pm
    "485": "itemtriggerrounding",   # rounding_1
    "486": "itemtriggerrounding",   # rounding_2
    "487": "bool",   # instant
    "488": "int",   # kerning
    "489": "bool",   # ignore_volume_test
    "490": "float",   # sound_duration
    "491": "bool",   # persistent
    "492": "bool",   # target_all
    "493": "bool",   # reset
    "494": "bool",   # timer
    "495": "bool",   # extra_sticky
    "496": "bool",   # dont_boost_y
    "497": "singlecolortype",   # single_color_type
    "498": "int",   # bpm
    "499": "bpmspeed",   # speed
    "500": "bool",   # disable
    "501": "int",   # bpb
    "502": "reverbtype",   # reverb_type
    "503": "bool",   # reverb_enable
    "504": "bool",   # spawn_only
    "505": "bool",   # unique_remap
    "506": "float",   # preview_opacity
    "507": "bool",   # no_particle
    "508": "bool",   # disable_all
    "509": "bool",   # dont_boost_x
    "510": "bool",   # snap_ground
    "511": "bool",   # extended_collision
    "512": "float",   # max_size
    "513": "bool",   # animate
    "514": "bool",   # relative
    "515": "bool",   # hard_edges
    "516": "groupid",   # min_x_id
    "517": "groupid",   # min_y_id
    "518": "groupid",   # max_x_id
    "519": "groupid",   # max_y_id
    "520": "float",   # time_mod
    "521": "float",   # position_x_mod
    "522": "float",   # rotation_mod
    "523": "float",   # scale_x_mod
    "524": "float",   # line_opacity
    "525": "int",   # extra_id_2
    "526": "float",   # min_force
    "527": "float",   # max_force
    "528": "bool",   # relative
    "529": "bool",   # range
    "530": "forceid",   # force_id
    "531": "bool",   # shader_disable
    "532": "optionset",   # hide_attempts
    "533": "background",   # background
    "534": "controlid",   # control_id
    "535": "bool",   # use_control_id
    "536": "keyframerotdir",   # cw_ccw
    "537": "int",   # x360
    "538": "areacenterspecial",   # center_special
    "539": "bool",   # de_ap
    "540": "bool",   # stop_jump
    "541": "bool",   # stop_move
    "542": "bool",   # stop_rot
    "543": "bool",   # stop_slide
    "544": "bool",   # silent
    "545": "float",   # position_y_mod
    "546": "float",   # scale_y_mod
    "547": "float",   # offset_x
    "548": "float",   # offset_y
    "549": "float",   # offvar_x
    "550": "float",   # offvar_y
    "551": "bool",   # match_rot
    "552": "float",   # particle_rotation
    "553": "float",   # particle_rotation_pm
    "554": "float",   # particle_scale
    "555": "float",   # particle_scale_pm
    "556": "float",   # delay_pm
    "557": "float",   # spawn_delay
    "558": "float",   # friction
    "559": "float",   # friction_pm
    "560": "int",   # start_speed_unmarked
    "561": "float",   # near_friction
    "562": "float",   # near_friction_pm
    "563": "int",   # start_dir
    "564": "int",   # start_dir_pm
    "565": "int",   # start_dir_unmarked
    "566": "float",   # mod_x
    "567": "float",   # mod_x_pm
    "568": "float",   # mod_y
    "569": "float",   # mod_y_pm
    "570": "bool",   # redirect_dir
    "571": "bool",   # exclusive
    "572": "advancedfollowmode",   # init_set_add
    "573": "optionset",   # edit_respawn_time
    "574": "float",   # respawn_time
    "575": "optionset",   # audio_on_death
    "576": "optionset",   # no_death_sfx
    "577": "bool",   # relative_scale
    "578": "itemtriggerabsneg",   # abs_neg_1
    "579": "itemtriggerabsneg",   # abs_neg_2
    "580": "stopmode",   # stop_pause_resume
    "581": "bool",   # reset_remap
    "582": "float",   # velocity_mod_x
    "583": "float",   # velocity_mod_y
    "584": "bool",   # override_velocity
    "585": "bool",   # dont_slide
    "586": "float",   # speed
    "587": "bool",   # allow_collide
    "588": "float",   # end_boost
    "589": "bool",   # stop_slide
    "590": "float",   # max_duration
    "591": "bool",   # redirect_dash
    "592": "bool",   # offset_anim
    "593": "optionset",   # boost_slide
    "595": "bool",   # dont_reset
    "596": "int",   # speed_pm
    "597": "int",   # pitch_pm
    "598": "float",   # volume_pm
    "599": "bool",   # pitch_steps
}

NAME_TO_ID = {
    'id': 1,
    'x': 2,
    'y': 3,
    'horizontal_flip': 4,
    'vertical_flip': 5,
    'rotation': 6,
    'trigger_red': 7,
    'trigger_green': 8,
    'trigger_blue': 9,
    'duration': 10,
    'touch_triggered': 11,
    'secret_coin_id' : 12,
    'portal_checked': 13,
    'tint_ground' : 14,
    'player_color_1': 15,
    'player_color_2': 16,
    'blending': 17,
    '1pt9_color_channel_id': 19,
    'editor_layer_1': 20,
    'color': 21,
    'color_2': 22,
    'target_color': 23,
    'z_layer': 24,
    'z_order': 25,
    'move_x': 28,
    'move_y': 29,
    'easing': 30,
    'text': 31,
    'scale': 32,
    'group_parent': 34,
    'opacity': 35,
    'active_trigger': 36,
    'hsv_enabled': 41,
    'color_2_hsv_enabled': 42,
    'hsv': 43,
    'color_2_hsv': 44,
    'fade_in': 45,
    'hold': 46,
    'fade_out': 47,
    'pulse_hsv': 48,
    'copied_color_hsv': 49,
    'copied_color_id': 50,
    'target': 51,
    'target_type': 52,
    'yellow_teleportation_portal_distance': 54,
    'activate_group': 56,
    'groups': 57,
    'lock_to_player_x': 58,
    'lock_to_player_y': 59,
    'copy_opacity': 60,
    'editor_layer_2': 61,
    'spawn_triggered': 62,
    'spawn_duration': 63,
    'dont_fade': 64,
    'main_only': 65,
    'detail_only': 66,
    'dont_enter': 67,
    'rotate_degrees': 68,
    'times_360': 69,
    'lock_object_rotation': 70,
    'target_pos': 71,
    'x_mod': 72,
    'y_mod': 73,
    'strength': 75,
    'animation_id': 76,
    'count': 77,
    'subtract_count': 78,
    'pickup_mode': 79,
    'item_id': 80,
    'hold_mode': 81,
    'toggle_mode': 82,
    'interval': 84,
    'easing_rate': 85,
    'exclusive': 86,
    'multi_trigger': 87,
    'comparison': 88,
    'dual_mode': 89,
    'speed': 90,
    'delay': 91,
    'y_offset': 92,
    'activate_on_exit': 93,
    'dynamic_block': 94,
    'block_b': 95,
    'glow_disabled': 96,
    'rotation_speed': 97,
    'disable_rotation': 98,
    'orb_multi_activate': 99,
    'use_target': 100,
    'target_pos_axes': 101,
    'editor_disable': 102,
    'high_detail': 103,
    'count_multi_activate': 104,
    'max_speed': 105,
    'randomize_start': 106,
    'animation_speed': 107,
    'linked_group': 108,
    'camera_zoom': 109,
    'free_mode': 111,
    'edit_free_cam_settings': 112,
    'free_cam_easing': 113,
    'free_cam_padding': 114,
    'ord': 115,
    'no_effects': 116,
    'reversed': 118,
    'song_start': 119,
    'time_mod': 120,
    'no_touch': 121,
    'animate_on_trigger': 123,
    'scale_x': 128,
    'scale_y': 129,
    'perspective_x': 131,
    'perspective_y': 132,
    'only_move': 133,
    'passable': 134,
    'hide': 135,
    'nonstick_x': 136,
    'ice_block': 137,
    'player_1': 138,
    'override_count': 139,
    'follow_camera_x': 141,
    'follow_camera_y': 142,
    'follow_camera_x_mod': 143,
    'follow_camera_y_mod': 144,
    'particle_setup': 145,
    'use_obj_color': 146,
    'gravity': 148,
    'scale_x_by': 150,
    'scale_y_by': 151,
    'group_probabilities': 152,
    'div_by_x': 153,
    'div_by_y': 154,
    'streak_additive': 159,
    'unlink_dual_gravity': 160,
    'hide_ground': 161,
    'hide_p1': 162,
    'hide_p2': 163,
    'camera_edge': 164,
    'keep_velocity': 169,
    'change_channel': 171,
    'grip_slope': 193,
    'hide_mg': 195,
    'player_only': 198,
    'disable_controls_p1': 199,
    'player_2': 200,
    '_pt': 201,
    'gradient_layer': 202,
    'gradient_bl': 203,
    'gradient_br': 204,
    'gradient_tl': 205,
    'gradient_tr': 206,
    'gradient_vertex_mode': 207,
    'gradient_disable': 208,
    'gradient_id': 209,
    'quick_start': 211,
    'follow_group': 212,
    'follow_easing': 213,
    'follow_p1': 215,
    'follow_p2': 216,
    'aream_move_dist': 218,
    'area_offset': 220,
    'area_length': 222,
    'effect_id': 225,
    'area_move_angle': 231,
    'area_scale_x': 233,
    'area_scale_y': 235,
    'area_move_x': 237,
    'area_move_y': 239,
    'area_xy_mode': 241,
    'area_easing': 242,
    'area_direction': 262,
    'mod_front': 263,
    'mod_back': 264,
    'parent_groups': 274,
    'area_inwards': 276,
    'area_parent': 279,
    'deadzone': 282,
    'area_mirrored': 283,
    'nonstick_y': 289,
    'effect_priority': 341,
    'enter_channel': 343,
    'scale_stick': 356,
    'disable_grid_snap': 370,
    'no_audio_scale': 372,
    'follow_mode': 394,
    'center_group_id': 395,
    'target_move_distance': 396,
    'rotation_dynamic': 397,
    'rotation_target': 401,
    'rotation_offset': 402,
    'events': 430,
    'sequence': 435,
    'seq_mode': 436,
    'seq_min_int': 437,
    'seq_reset': 438,
    'seq_reset_type': 439,
    'spawn_ordered': 441,
    'spawn_remap': 442,
    'material': 446,
    'pickup_mod': 449,
    'preview_opacity': 456,
    'timer_display': 466,
    'timer_start': 467,
    'no_timer_override': 468,
    'ignore_time_warp': 469,
    'timer_mod': 470,
    'timer_paused': 471,
    'timer_control': 472,
    'timer_target': 473,
    'timer_stop': 474,
    'timer_multi_active': 475,
    'item_type_1': 476,
    'item_type_2': 477,
    'item_type_3': 478,
    'num_mod': 479,
    'num_op_1': 480,
    'num_op_2': 481,
    'num_op_3': 482,
    'num_mod_2': 483,
    'num_offset': 484,
    'round_op_1': 485,
    'round_op_2': 486,
    'set_persistent': 491,
    'pers_target_all': 492,
    'pers_reset': 493,
    'pers_timer': 494,
    'extra_sticky': 495,
    'dont_boost_y': 496,
    'seq_unique_remap': 505,
    'no_particle': 507,
    'dont_boost_x': 509,
    'extended_collision': 511,
    'event_target': 525,
    'dont_edit_area_parent': 539,
    'neg_op_1': 578,
    'neg_op_2': 579,
}

if __name__ == "__main__":
    pass