__author__ = 'Lothilius'
# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Enum, Float, Index, Integer, Numeric, SmallInteger, String, Text, VARBINARY, text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta


Base = declarative_base()
metadata = Base.metadata

current_time = datetime.now()


class HitTypeSetting(Base):
    __tablename__ = u'HitTypeSettings'

    id = Column(Integer, primary_key=True)
    Title = Column(String(255), nullable=False)
    Description = Column(Text, nullable=False)
    Keywords = Column(String(255))
    Price = Column(Numeric(4, 3), nullable=False)
    Bonus_Price = Column(Numeric(4, 3), nullable=False)
    Question = Column(Text, nullable=False)
    AwsId = Column(String(255), nullable=False)
    AwsKey = Column(String(255), nullable=False)
    Sandbox = Column(Integer, nullable=False)
    HitTypeId = Column(String(255), nullable=False)
    debug = Column(Integer, nullable=False)
    formUrl = Column(String(255), nullable=False)
    AssignmentDuration = Column(Integer, nullable=False)
    RepostDays = Column(Integer, nullable=False)
    notification_url = Column(String(255), nullable=False)


class Hit(Base):
    __tablename__ = u'Hits'

    mtid = Column(Integer, primary_key=True)
    hitid = Column(String(200), nullable=False)
    mtvenueid = Column(Integer, nullable=False)
    date_published = Column(DateTime)
    last_published = Column(DateTime)
    next_publishdate = Column(DateTime)
    mt_status = Column(Enum(u'0', u'1', u'2'), nullable=False, server_default=text("'0'"))


class AdminLog(Base):
    __tablename__ = u'admin_log'

    id = Column(Integer, primary_key=True)
    admin_id = Column(Integer, nullable=False)
    role_name = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    requested_resource = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    permission_granted = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    ip_address = Column(String(255, u'utf8_unicode_ci'), nullable=False)
    request_date = Column(DateTime, nullable=False)


class AdminResource(Base):
    __tablename__ = u'admin_resource'

    resource_id = Column(Integer, primary_key=True)
    resource_name = Column(String(255), nullable=False)


class AdminRole(Base):
    __tablename__ = u'admin_role'

    id = Column(Integer, primary_key=True)
    role_name = Column(String(128), nullable=False)


class AdminRule(Base):
    __tablename__ = u'admin_rule'

    rule_id = Column(Integer, primary_key=True)
    role_id = Column(Integer, nullable=False)
    resource_id = Column(Integer, nullable=False)
    access_permission = Column(String(255), nullable=False)


class AdminSetting(Base):
    __tablename__ = u'admin_settings'

    id = Column(Integer, primary_key=True)
    single_column_list_no = Column(Integer, nullable=False)
    total_events_at_eventslist = Column(Integer, nullable=False, server_default=text("'50'"))
    display_at_todayspic = Column(Enum(u'e', u'a'), nullable=False, server_default=text("'e'"))
    datp_event_id = Column(Integer, server_default=text("'0'"))
    max_shared_advt = Column(Integer, nullable=False, server_default=text("'15'"))
    dasv_venue_id = Column(String(255))
    placement_position_1 = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    placement_position_2 = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    placement_position_3 = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    placement_position_4 = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    placement_position_5 = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    placement_position_1_advt_details_id = Column(Integer, nullable=False, server_default=text("'0'"))
    placement_position_2_advt_details_id = Column(Integer, nullable=False, server_default=text("'0'"))
    placement_position_3_advt_details_id = Column(Integer, nullable=False, server_default=text("'0'"))
    placement_position_4_advt_details_id = Column(Integer, nullable=False, server_default=text("'0'"))
    placement_position_5_advt_details_id = Column(Integer, nullable=False, server_default=text("'0'"))
    tweet_userid = Column(String(255), nullable=False)
    tweet_count = Column(Integer, nullable=False, server_default=text("'5'"))
    facebook_page_username = Column(String(255), nullable=False)
    fb_category = Column(Integer)
    fb_subcategory = Column(Integer)
    total_pending_events_for_admin_mail_trigger = Column(Integer, nullable=False, server_default=text("'15'"))
    admin_fb_uid = Column(String(255))
    admin_fb_access_token = Column(Text)
    admin_fb_email = Column(String(255))
    admin_fb_first_name = Column(String(255))
    admin_fb_last_name = Column(String(255))


class AdminUser(Base):
    __tablename__ = u'admin_user'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, nullable=False)
    username = Column(String(40), nullable=False)
    password = Column(String(32), nullable=False)
    created = Column(DateTime, nullable=False)
    lastlogin = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    pending_list_subscribe = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'0'"))
    status = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'1'"))


class AdvtCurrent(Base):
    __tablename__ = u'advt_current'

    id = Column(Integer, primary_key=True)
    space_type = Column(String(1), nullable=False)
    advt_details_id = Column(Integer, nullable=False)
    placement_position_id = Column(Integer, nullable=False)


class AdvtDetail(Base):
    __tablename__ = u'advt_details'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    refund_at_this_email = Column(String(255))
    desc = Column(Text, nullable=False)
    purpose = Column(Text, nullable=False)
    space_type = Column(String(1), nullable=False)
    placement_position_id = Column(Integer, nullable=False)
    advt_type = Column(String(1), nullable=False)
    total_duration = Column(Float, nullable=False)
    total_impression = Column(BigInteger, nullable=False)
    total_cost = Column(Float, nullable=False)
    url_link = Column(String(255), nullable=False)
    advt_file = Column(Text)
    upload_later = Column(Integer)
    want_a_design = Column(Integer, nullable=False)
    date_added = Column(DateTime, nullable=False)
    url_encrypt = Column(Text)
    paid = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    advt_details_status = Column(Enum(u'0', u'1', u'2'), nullable=False, server_default=text("'0'"))
    is_expired = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    godrt = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))


class AdvtPrice(Base):
    __tablename__ = u'advt_prices'

    id = Column(Integer, primary_key=True)
    placement_position_id = Column(Integer, nullable=False)
    premium_price = Column(Float, nullable=False)
    monthly_price = Column(Float, nullable=False)
    weekly_price = Column(Float, nullable=False)
    daily_price = Column(Float, nullable=False)
    per_impression_price = Column(Float, nullable=False)
    max_advts = Column(Integer, nullable=False, server_default=text("'50'"))


class AdvtRestricted(Base):
    __tablename__ = u'advt_restricted'

    id = Column(Integer, primary_key=True)
    advt_details_id = Column(Integer, nullable=False)
    useridd = Column(Integer, nullable=False)
    placement_position_id = Column(Integer, nullable=False)
    url_link = Column(String(255), nullable=False)
    advt_file = Column(Text, nullable=False)
    total_duration = Column(Float, nullable=False)
    total_impression = Column(BigInteger, nullable=False)
    remaining_duration = Column(Float, nullable=False)
    remaining_impression = Column(BigInteger, nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_activated = Column(DateTime)
    status = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    is_expired = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))


class AdvtShared(Base):
    __tablename__ = u'advt_shared'

    id = Column(Integer, primary_key=True)
    advt_details_id = Column(Integer, nullable=False)
    useridd = Column(Integer, nullable=False)
    placement_position_id = Column(Integer, nullable=False)
    url_link = Column(String(255), nullable=False)
    advt_file = Column(Text)
    total_duration = Column(Float, nullable=False)
    total_impression = Column(BigInteger, nullable=False)
    remaining_duration = Column(Float, nullable=False)
    remaining_impression = Column(BigInteger, nullable=False)
    date_added = Column(DateTime, nullable=False)
    date_activated = Column(DateTime)
    status = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    is_expired = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))


class Category(Base):
    __tablename__ = u'category'

    id = Column(Integer, primary_key=True)
    category_name = Column(String(40), nullable=False)
    icon = Column(String(100, u'utf8_unicode_ci'), nullable=False, server_default=text("'oi915_iphone.png'"))
    category_desc = Column(String(128), nullable=False)
    meta_keywords = Column(String(128))
    meta_title = Column(String(40))
    meta_desc = Column(String(128))
    category_pagetitle = Column(String(128), nullable=False)
    category_order = Column(Integer, nullable=False)
    category_status = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'1'"))
    color = Column(String(100), nullable=False, server_default=text("'blue'"))


class Comment(Base):
    __tablename__ = u'comment'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    comment = Column(Text, nullable=False)
    comment_start = Column(DateTime, nullable=False)


class Corepage(Base):
    __tablename__ = u'corepages'

    id = Column(Integer, primary_key=True)
    about = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    contact = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    faq = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    promos = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    freebies = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    giveaways = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    hosted = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    emails = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    friendemail = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    register = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    want_a_design = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)
    privacy_policy = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)


class Event(Base):
    __tablename__ = u'event'

    id = Column(Integer, primary_key=True)
    fb_eventid = Column(String(255))
    group_id = Column(String(20))
    category_id = Column(VARBINARY(255), nullable=False)
    subcat_id = Column(String(255), nullable=False)
    user_id = Column(Integer)
    event_name = Column(String(255), nullable=False)
    event_desc = Column(Text, nullable=False)
    is_venue_name_filled = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'1'"))
    venue_id = Column(Integer, nullable=False)
    event_start = Column(DateTime, nullable=False)
    event_end = Column(DateTime, nullable=False)
    event_repeat = Column(String(255), nullable=False, server_default=text("'o'"))
    event_repeat_end = Column(DateTime)
    event_source = Column(String(255))
    event_source_title = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zipcode = Column(String(255))
    image = Column(String(255), nullable=False, server_default=text("'oi915_fillerpic.png'"))
    status = Column(Enum(u'1', u'0', u'2'), nullable=False, server_default=text("'2'"))
    how = Column(Text)
    sftp = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    asedrt = Column(String(255))
    event_added = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    who = Column(Text, nullable=False)
    week = Column(Integer, nullable=False)
    type = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    hit_id = Column(String(255))
    assignment_id = Column(String(255))
    worker_id = Column(String(200))
    pstart = Column(DateTime)
    pend = Column(DateTime)
    wall_post_title = Column(Text)
    event_post_to_facebook = Column(Integer, nullable=False, server_default=text("'0'"))
    block_post = Column(Integer, nullable=False, server_default=text("'0'"))

    def __init__(self, event, category_id='1', subcat_id='8', user_id='6', is_venue_name_filled='1',
                 event_end='', event_repeat='o', sftp='0',
                 event_added=current_time.strftime('%Y-%m-%d %H:%M:%S'), who='', week='0', type_col='0',
                 event_post_to_facebook='0', block_post='0'):

        if event_end == '':
            event_end = datetime.strptime(event[5], '%Y-%m-%d %H:%M:%S')
            event_end += timedelta(hours=3)



        self.fb_eventid = event[0]
        self.event_name = event[1]
        self.event_desc = event[2]
        self.venue_id = event[3]
        self.event_start = event[5]
        self.event_source = event[6]
        self.event_source_title = event[7]
        self.image = event[8]
        self.how = event[9]
        self.status = event[10]
        self.category_id = category_id
        self.subcat_id = subcat_id
        self.user_id = user_id
        self.is_venue_name_filled = is_venue_name_filled
        self.event_end = event_end
        self.event_repeat = event_repeat
        self.sftp = sftp
        self.event_added = event_added
        self.who = who
        self.week = week
        self.type = type_col
        self.event_post_to_facebook = event_post_to_facebook
        self.block_post = block_post



class EventBackup05082012(Base):
    __tablename__ = u'event_backup_05_08_2012'

    id = Column(Integer, primary_key=True)
    fb_eventid = Column(String(255))
    group_id = Column(String(20))
    category_id = Column(VARBINARY(255), nullable=False)
    subcat_id = Column(String(255), nullable=False)
    user_id = Column(Integer)
    event_name = Column(String(255), nullable=False)
    event_desc = Column(Text, nullable=False)
    is_venue_name_filled = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'1'"))
    venue_id = Column(Integer, nullable=False)
    event_start = Column(DateTime, nullable=False)
    event_end = Column(DateTime, nullable=False)
    event_repeat = Column(String(255), nullable=False, server_default=text("'o'"))
    event_repeat_end = Column(DateTime)
    event_source = Column(String(255))
    event_source_title = Column(String(255))
    address = Column(String(255))
    city = Column(String(255))
    state = Column(String(255))
    zipcode = Column(String(255))
    image = Column(String(255), nullable=False, server_default=text("'oi915_fillerpic.png'"))
    status = Column(Enum(u'1', u'0', u'2'), nullable=False, server_default=text("'2'"))
    how = Column(Text)
    sftp = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    asedrt = Column(String(255))
    event_added = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    who = Column(Text, nullable=False)
    week = Column(Integer, nullable=False)
    type = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    hit_id = Column(String(255))
    assignment_id = Column(String(255))
    worker_id = Column(String(200))


class Eventcounter(Base):
    __tablename__ = u'eventcounter'

    id = Column(Integer, primary_key=True)
    counter = Column(Integer, nullable=False, server_default=text("'0'"))
    mailevent = Column(String(255), nullable=False)


class FbEventTempStorage(Base):
    __tablename__ = u'fb_event_temp_storage'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    event_data = Column(Text(collation=u'utf8_unicode_ci'), nullable=False)


class FbEventToken(Base):
    __tablename__ = u'fb_event_token'

    pkid = Column(Integer, primary_key=True)
    token_id = Column(Text, nullable=False)
    stag = Column(String)


class FbWallPost(Base):
    __tablename__ = u'fb_wall_posts'

    fb_wall_post_id = Column(Integer, primary_key=True)
    fb_message = Column(Text)
    fb_title = Column(Text)
    fb_posting_time = Column(DateTime)
    fb_creation_time = Column(DateTime)


class FrontUser(Base):
    __tablename__ = u'front_user'

    id = Column(Integer, primary_key=True)
    fb_uid = Column(String(255))
    fb_access_token = Column(Text)
    email = Column(String(100), nullable=False)
    password = Column(String(32), nullable=False)
    created = Column(DateTime, nullable=False)
    lastlogin = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    address = Column(Text, nullable=False)
    city = Column(String(50), nullable=False, server_default=text("'.....'"))
    country = Column(String(50), nullable=False, server_default=text("'.....'"))
    dob = Column(Date, nullable=False)
    image = Column(String(255), nullable=False, server_default=text("'oi915_fillerpic.png'"))
    edit_rights = Column(String(255))
    verified = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    varify_url = Column(String(255))
    amount = Column(Float, nullable=False, server_default=text("'0'"))
    fb_eventid_uploaded = Column(Text)


class GoogleAdsense(Base):
    __tablename__ = u'google_adsense'

    id = Column(Integer, primary_key=True)
    placement_position_id = Column(Integer)
    google_adsense_code = Column(Text)


class LastCheckedEvent(Base):
    __tablename__ = u'last_checked_event'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False, server_default=text("'0'"))
    to_delete_event_ids = Column(String(255), nullable=False)


class Like(Base):
    __tablename__ = u'like'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    event_id = Column(Integer, nullable=False)
    like_start = Column(DateTime, nullable=False)
    like_count = Column(Integer, nullable=False)

    def __init__(self, user_id, event_id, like_start, like_count=0):

        self.user_id = user_id
        self.event_id = event_id
        self.like_start = like_start
        self.like_count = like_count


class Likecount(Base):
    __tablename__ = u'likecount'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, nullable=False)
    like_count = Column(Integer, nullable=False)

    def __init__(self, event_id, like_count=1):

        self.event_id = event_id
        self.like_count = like_count


class Location(Base):
    __tablename__ = u'location'

    id = Column(Integer, primary_key=True)
    location_name = Column(String(255), nullable=False)
    location_status = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'1'"))


class MtLog(Base):
    __tablename__ = u'mt_log'

    id = Column(Integer, primary_key=True)
    lvl = Column(Integer, nullable=False)
    msg = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class PaymentPaypalOrder(Base):
    __tablename__ = u'payment_paypal_order'

    id = Column(Integer, primary_key=True)
    advt_details_id = Column(Integer, nullable=False)
    trans_id = Column(String(128))
    card_type = Column(String(32))
    card_number = Column(String(64))
    card_expires = Column(String(16))
    token = Column(String(255))
    correlationid = Column(String(255))


class Resetpas(Base):
    __tablename__ = u'resetpass'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    link = Column(String(255, u'utf8_unicode_ci'))
    status = Column(Enum(u'1', u'0'), server_default=text("'1'"))


class Shbptc(Base):
    __tablename__ = u'shbptc'

    id = Column(Integer, primary_key=True)
    shbptc_image = Column(String(255), nullable=False)
    shbptc_desc = Column(Text, nullable=False)
    artist_name = Column(Text, nullable=False)
    artist_page = Column(Text)


class ShbptcVote(Base):
    __tablename__ = u'shbptc_votes'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, nullable=False)
    image_id = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)
    source = Column(Text)


class Subcategory(Base):
    __tablename__ = u'subcategory'

    id = Column(Integer, primary_key=True)
    parent_catid = Column(Integer, nullable=False)
    subcategory_name = Column(String(255), nullable=False)
    subcategory_status = Column(Integer, nullable=False, server_default=text("'1'"))


class Venue(Base):
    __tablename__ = u'venue'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    name = Column(String(128), nullable=False)
    location_id = Column(Integer, nullable=False, server_default=text("'0'"))
    addline1 = Column(String(255), nullable=False)
    addline2 = Column(String(255))
    city = Column(String(255), nullable=False)
    state = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    zip = Column(Integer, nullable=False)
    website = Column(String(255), nullable=False)
    image = Column(String(255), server_default=text("'oi915_fillerpic.png'"))
    phone = Column(BigInteger, nullable=False)
    lat = Column(Float(10), nullable=False, server_default=text("'0.000000'"))
    lng = Column(Float(10), nullable=False, server_default=text("'0.000000'"))
    timezone = Column(String(10), nullable=False, server_default=text("'+00'"))
    sizzvenue = Column(Enum(u'1', u'0'), nullable=False, server_default=text("'0'"))
    status = Column(Enum(u'0', u'1'), nullable=False, server_default=text("'1'"))
    desc = Column(Text, nullable=False)
    fb_venueid = Column(Integer)


class WpCommentmeta(Base):
    __tablename__ = u'wp_commentmeta'

    meta_id = Column(BigInteger, primary_key=True)
    comment_id = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(String)


class WpComment(Base):
    __tablename__ = u'wp_comments'
    __table_args__ = (
        Index(u'comment_approved_date_gmt', u'comment_approved', u'comment_date_gmt'),
    )

    comment_ID = Column(BigInteger, primary_key=True)
    comment_post_ID = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    comment_author = Column(String, nullable=False)
    comment_author_email = Column(String(100), nullable=False, server_default=text("''"))
    comment_author_url = Column(String(200), nullable=False, server_default=text("''"))
    comment_author_IP = Column(String(100), nullable=False, server_default=text("''"))
    comment_date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    comment_date_gmt = Column(DateTime, nullable=False, index=True, server_default=text("'0000-00-00 00:00:00'"))
    comment_content = Column(Text, nullable=False)
    comment_karma = Column(Integer, nullable=False, server_default=text("'0'"))
    comment_approved = Column(String(20), nullable=False, server_default=text("'1'"))
    comment_agent = Column(String(255), nullable=False, server_default=text("''"))
    comment_type = Column(String(20), nullable=False, server_default=text("''"))
    comment_parent = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    user_id = Column(BigInteger, nullable=False, server_default=text("'0'"))


class WpEshopBaseProduct(Base):
    __tablename__ = u'wp_eshop_base_products'

    post_id = Column(BigInteger, primary_key=True, server_default=text("'0'"))
    img = Column(Text, nullable=False)
    brand = Column(String(255), nullable=False, server_default=text("''"))
    ptype = Column(String(255), nullable=False, server_default=text("''"))
    thecondition = Column(String(255), nullable=False, server_default=text("''"))
    expiry = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    ean = Column(String(255), nullable=False, server_default=text("''"))
    isbn = Column(String(255), nullable=False, server_default=text("''"))
    mpn = Column(String(255), nullable=False, server_default=text("''"))
    qty = Column(Integer, nullable=False, server_default=text("'0'"))
    xtra = Column(Text, nullable=False)


class WpEshopCountry(Base):
    __tablename__ = u'wp_eshop_countries'

    code = Column(String(2), primary_key=True, server_default=text("''"))
    country = Column(String(50), nullable=False, server_default=text("''"))
    zone = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    list = Column(Integer, nullable=False, server_default=text("'1'"))


class WpEshopDiscountCode(Base):
    __tablename__ = u'wp_eshop_discount_codes'

    id = Column(Integer, primary_key=True)
    dtype = Column(Integer, nullable=False, server_default=text("'0'"))
    disccode = Column(String(255), nullable=False, unique=True, server_default=text("''"))
    percent = Column(Float(5), nullable=False, server_default=text("'0.00'"))
    remain = Column(String(11), nullable=False, server_default=text("''"))
    used = Column(Integer, nullable=False, server_default=text("'0'"))
    enddate = Column(Date, nullable=False, server_default=text("'0000-00-00'"))
    live = Column(String(3), nullable=False, server_default=text("'no'"))


class WpEshopDownloadOrder(Base):
    __tablename__ = u'wp_eshop_download_orders'
    __table_args__ = (
        Index(u'code', u'code', u'email'),
    )

    id = Column(Integer, primary_key=True)
    checkid = Column(String(255), nullable=False, server_default=text("''"))
    title = Column(String(255), nullable=False, server_default=text("''"))
    purchased = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    files = Column(String(255), nullable=False, server_default=text("''"))
    downloads = Column(SmallInteger, nullable=False, server_default=text("'3'"))
    code = Column(String(20), nullable=False, server_default=text("''"))
    email = Column(String(255), nullable=False, server_default=text("''"))


class WpEshopDownload(Base):
    __tablename__ = u'wp_eshop_downloads'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False, server_default=text("''"))
    added = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    files = Column(String(255), nullable=False, server_default=text("''"))
    downloads = Column(Integer, nullable=False, server_default=text("'0'"))
    purchases = Column(Integer, nullable=False, server_default=text("'0'"))


class WpEshopEmail(Base):
    __tablename__ = u'wp_eshop_emails'

    id = Column(Integer, primary_key=True)
    emailUse = Column(Integer, nullable=False, server_default=text("'0'"))
    emailType = Column(String(50), nullable=False, server_default=text("''"))
    emailSubject = Column(String(255), nullable=False, server_default=text("''"))
    emailContent = Column(Text, nullable=False)


class WpEshopOptionName(Base):
    __tablename__ = u'wp_eshop_option_names'

    optid = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, server_default=text("''"))
    admin_name = Column(String(255), nullable=False, server_default=text("''"))
    type = Column(Integer, nullable=False, server_default=text("'0'"))
    description = Column(String(255), nullable=False, server_default=text("''"))


class WpEshopOptionSet(Base):
    __tablename__ = u'wp_eshop_option_sets'

    id = Column(Integer, primary_key=True)
    optid = Column(Integer, nullable=False, server_default=text("'0'"))
    name = Column(String(255), nullable=False, server_default=text("''"))
    price = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    weight = Column(Float(8), nullable=False, server_default=text("'0.00'"))


class WpEshopOrderItem(Base):
    __tablename__ = u'wp_eshop_order_items'

    id = Column(Integer, primary_key=True)
    checkid = Column(String(255), nullable=False, index=True, server_default=text("''"))
    item_id = Column(String(255), nullable=False, server_default=text("'0'"))
    item_qty = Column(Integer, nullable=False, server_default=text("'0'"))
    item_amt = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    tax_rate = Column(String(255), nullable=False, server_default=text("''"))
    tax_amt = Column(String(255), nullable=False, server_default=text("''"))
    optname = Column(String(255), nullable=False, server_default=text("''"))
    optsets = Column(Text, nullable=False)
    post_id = Column(Integer, nullable=False, server_default=text("'0'"))
    option_id = Column(Integer, nullable=False, server_default=text("'0'"))
    down_id = Column(Integer, nullable=False, server_default=text("'0'"))
    weight = Column(Float(16), nullable=False, server_default=text("'0.00'"))


class WpEshopOrder(Base):
    __tablename__ = u'wp_eshop_orders'

    id = Column(Integer, primary_key=True)
    checkid = Column(String(255), nullable=False, index=True, server_default=text("''"))
    status = Column(String(9), nullable=False, index=True, server_default=text("'Pending'"))
    first_name = Column(String(50), nullable=False, server_default=text("''"))
    last_name = Column(String(50), nullable=False, server_default=text("''"))
    company = Column(String(255), nullable=False, server_default=text("''"))
    email = Column(String(100), nullable=False, server_default=text("''"))
    phone = Column(String(30), nullable=False, server_default=text("''"))
    address1 = Column(String(255), nullable=False, server_default=text("''"))
    address2 = Column(String(255), nullable=False, server_default=text("''"))
    city = Column(String(100), nullable=False, server_default=text("''"))
    state = Column(String(100), nullable=False, server_default=text("''"))
    zip = Column(String(20), nullable=False, server_default=text("''"))
    country = Column(String(3), nullable=False, server_default=text("''"))
    reference = Column(String(255), nullable=False, server_default=text("''"))
    ship_name = Column(String(100), nullable=False, server_default=text("''"))
    ship_company = Column(String(255), nullable=False, server_default=text("''"))
    ship_phone = Column(String(30), nullable=False, server_default=text("''"))
    ship_address = Column(String(255), nullable=False, server_default=text("''"))
    ship_city = Column(String(100), nullable=False, server_default=text("''"))
    ship_state = Column(String(100), nullable=False, server_default=text("''"))
    ship_postcode = Column(String(20), nullable=False, server_default=text("''"))
    ship_country = Column(String(3), nullable=False, server_default=text("''"))
    custom_field = Column(String(15), nullable=False, server_default=text("''"))
    transid = Column(String(255), nullable=False, server_default=text("''"))
    comments = Column(Text, nullable=False)
    thememo = Column(Text, nullable=False)
    edited = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    downloads = Column(String(3), nullable=False, server_default=text("'no'"))
    admin_note = Column(Text, nullable=False)
    paidvia = Column(String(255), nullable=False, server_default=text("''"))
    affiliate = Column(String(255), nullable=False, server_default=text("''"))
    user_id = Column(Integer, nullable=False)
    user_notes = Column(Text, nullable=False)


class WpEshopRate(Base):
    __tablename__ = u'wp_eshop_rates'

    id = Column(Integer, primary_key=True)
    _class = Column(u'class', String(3), nullable=False, server_default=text("''"))
    items = Column(SmallInteger, nullable=False, server_default=text("'0'"))
    zone1 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    zone2 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    zone3 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    zone4 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    zone5 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    zone6 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    zone7 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    zone8 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    zone9 = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    weight = Column(Float(16), nullable=False, server_default=text("'0.00'"))
    maxweight = Column(String(16), nullable=False, server_default=text("''"))
    area = Column(String(50), nullable=False, server_default=text("''"))
    rate_type = Column(String(255), nullable=False, server_default=text("'shipping'"))


class WpEshopState(Base):
    __tablename__ = u'wp_eshop_states'

    id = Column(Integer, primary_key=True)
    code = Column(String(4), nullable=False, server_default=text("''"))
    stateName = Column(String(30), nullable=False, server_default=text("''"))
    zone = Column(Integer, nullable=False, index=True, server_default=text("'0'"))
    list = Column(String(2), nullable=False, server_default=text("''"))


class WpEshopStock(Base):
    __tablename__ = u'wp_eshop_stock'
    __table_args__ = (
        Index(u'post_id', u'post_id', u'available', u'purchases'),
    )

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, nullable=False, server_default=text("'0'"))
    option_id = Column(Integer, nullable=False, server_default=text("'0'"))
    available = Column(Integer, nullable=False, server_default=text("'0'"))
    purchases = Column(Integer, nullable=False, server_default=text("'0'"))


class WpHlTwitterReply(Base):
    __tablename__ = u'wp_hl_twitter_replies'

    id = Column(Integer, primary_key=True)
    twitter_tweet_id = Column(BigInteger, unique=True)
    twitter_user_id = Column(Integer)
    twitter_user_name = Column(String(40, u'utf8_unicode_ci'))
    twitter_user_screen_name = Column(String(40, u'utf8_unicode_ci'))
    twitter_user_url = Column(String(255, u'utf8_unicode_ci'))
    twitter_user_avatar = Column(String(255, u'utf8_unicode_ci'))
    tweet = Column(String(160, u'utf8_unicode_ci'), index=True)
    lat = Column(Float(asdecimal=True))
    lon = Column(Float(asdecimal=True))
    created = Column(DateTime)
    reply_tweet_id = Column(BigInteger)
    reply_user_id = Column(Integer)
    reply_screen_name = Column(String(40, u'utf8_unicode_ci'))
    source = Column(String(40, u'utf8_unicode_ci'))


class WpHlTwitterTweet(Base):
    __tablename__ = u'wp_hl_twitter_tweets'

    id = Column(Integer, primary_key=True)
    twitter_tweet_id = Column(BigInteger, unique=True)
    twitter_user_id = Column(Integer, index=True)
    tweet = Column(String(160, u'utf8_unicode_ci'), index=True)
    lat = Column(Float(asdecimal=True))
    lon = Column(Float(asdecimal=True))
    created = Column(DateTime)
    reply_tweet_id = Column(BigInteger)
    reply_user_id = Column(Integer)
    reply_screen_name = Column(String(40, u'utf8_unicode_ci'))
    source = Column(String(40, u'utf8_unicode_ci'))


class WpHlTwitterUser(Base):
    __tablename__ = u'wp_hl_twitter_users'

    id = Column(Integer, primary_key=True)
    twitter_user_id = Column(Integer, index=True)
    screen_name = Column(String(40, u'utf8_unicode_ci'))
    name = Column(String(40, u'utf8_unicode_ci'))
    num_friends = Column(Integer)
    num_followers = Column(Integer)
    num_tweets = Column(Integer)
    registered = Column(DateTime)
    url = Column(String(255, u'utf8_unicode_ci'))
    description = Column(String(255, u'utf8_unicode_ci'))
    location = Column(String(40, u'utf8_unicode_ci'))
    avatar = Column(String(255, u'utf8_unicode_ci'))
    created = Column(DateTime)
    last_updated = Column(DateTime)
    pull_in_replies = Column(Integer, server_default=text("'0'"))


class WpInstagram(Base):
    __tablename__ = u'wp_instagram'

    access_token = Column(String(150, u'utf8_unicode_ci'), nullable=False)
    user_id = Column(String(50, u'utf8_unicode_ci'), nullable=False)
    ID = Column(Integer, primary_key=True)


class WpLink(Base):
    __tablename__ = u'wp_links'

    link_id = Column(BigInteger, primary_key=True)
    link_url = Column(String(255), nullable=False, server_default=text("''"))
    link_name = Column(String(255), nullable=False, server_default=text("''"))
    link_image = Column(String(255), nullable=False, server_default=text("''"))
    link_target = Column(String(25), nullable=False, server_default=text("''"))
    link_description = Column(String(255), nullable=False, server_default=text("''"))
    link_visible = Column(String(20), nullable=False, index=True, server_default=text("'Y'"))
    link_owner = Column(BigInteger, nullable=False, server_default=text("'1'"))
    link_rating = Column(Integer, nullable=False, server_default=text("'0'"))
    link_updated = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    link_rel = Column(String(255), nullable=False, server_default=text("''"))
    link_notes = Column(String, nullable=False)
    link_rss = Column(String(255), nullable=False, server_default=text("''"))


class WpNggAlbum(Base):
    __tablename__ = u'wp_ngg_album'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    previewpic = Column(BigInteger, nullable=False, server_default=text("'0'"))
    albumdesc = Column(String)
    sortorder = Column(String, nullable=False)
    pageid = Column(BigInteger, nullable=False, server_default=text("'0'"))


class WpNggGallery(Base):
    __tablename__ = u'wp_ngg_gallery'

    gid = Column(BigInteger, primary_key=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    path = Column(String)
    title = Column(String)
    galdesc = Column(String)
    pageid = Column(BigInteger, nullable=False, server_default=text("'0'"))
    previewpic = Column(BigInteger, nullable=False, server_default=text("'0'"))
    author = Column(BigInteger, nullable=False, server_default=text("'0'"))


class WpNggPicture(Base):
    __tablename__ = u'wp_ngg_pictures'

    pid = Column(BigInteger, primary_key=True)
    image_slug = Column(String(255), nullable=False)
    post_id = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    galleryid = Column(BigInteger, nullable=False, server_default=text("'0'"))
    filename = Column(String(255), nullable=False)
    description = Column(String)
    alttext = Column(String)
    imagedate = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    exclude = Column(Integer, server_default=text("'0'"))
    sortorder = Column(BigInteger, nullable=False, server_default=text("'0'"))
    meta_data = Column(String)


class WpOption(Base):
    __tablename__ = u'wp_options'

    option_id = Column(BigInteger, primary_key=True)
    option_name = Column(String(64), nullable=False, unique=True, server_default=text("''"))
    option_value = Column(String, nullable=False)
    autoload = Column(String(20), nullable=False, server_default=text("'yes'"))


class WpPostmeta(Base):
    __tablename__ = u'wp_postmeta'

    meta_id = Column(BigInteger, primary_key=True)
    post_id = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(String)


class WpPost(Base):
    __tablename__ = u'wp_posts'
    __table_args__ = (
        Index(u'type_status_date', u'post_type', u'post_status', u'post_date', u'ID'),
    )

    ID = Column(BigInteger, primary_key=True)
    post_author = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    post_date = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_date_gmt = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_content = Column(String, nullable=False)
    post_title = Column(Text, nullable=False)
    post_excerpt = Column(Text, nullable=False)
    post_status = Column(String(20), nullable=False, server_default=text("'publish'"))
    comment_status = Column(String(20), nullable=False, server_default=text("'open'"))
    ping_status = Column(String(20), nullable=False, server_default=text("'open'"))
    post_password = Column(String(20), nullable=False, server_default=text("''"))
    post_name = Column(String(200), nullable=False, index=True, server_default=text("''"))
    to_ping = Column(Text, nullable=False)
    pinged = Column(Text, nullable=False)
    post_modified = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_modified_gmt = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    post_content_filtered = Column(String, nullable=False)
    post_parent = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    guid = Column(String(255), nullable=False, server_default=text("''"))
    menu_order = Column(Integer, nullable=False, server_default=text("'0'"))
    post_type = Column(String(20), nullable=False, server_default=text("'post'"))
    post_mime_type = Column(String(100), nullable=False, server_default=text("''"))
    comment_count = Column(BigInteger, nullable=False, server_default=text("'0'"))


class WpTermRelationship(Base):
    __tablename__ = u'wp_term_relationships'

    object_id = Column(BigInteger, primary_key=True, nullable=False, server_default=text("'0'"))
    term_taxonomy_id = Column(BigInteger, primary_key=True, nullable=False, index=True, server_default=text("'0'"))
    term_order = Column(Integer, nullable=False, server_default=text("'0'"))


class WpTermTaxonomy(Base):
    __tablename__ = u'wp_term_taxonomy'
    __table_args__ = (
        Index(u'term_id_taxonomy', u'term_id', u'taxonomy', unique=True),
    )

    term_taxonomy_id = Column(BigInteger, primary_key=True)
    term_id = Column(BigInteger, nullable=False, server_default=text("'0'"))
    taxonomy = Column(String(32), nullable=False, index=True, server_default=text("''"))
    description = Column(String, nullable=False)
    parent = Column(BigInteger, nullable=False, server_default=text("'0'"))
    count = Column(BigInteger, nullable=False, server_default=text("'0'"))


class WpTerm(Base):
    __tablename__ = u'wp_terms'

    term_id = Column(BigInteger, primary_key=True)
    name = Column(String(200), nullable=False, index=True, server_default=text("''"))
    slug = Column(String(200), nullable=False, unique=True, server_default=text("''"))
    term_group = Column(BigInteger, nullable=False, server_default=text("'0'"))


class WpUsermeta(Base):
    __tablename__ = u'wp_usermeta'

    umeta_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, nullable=False, index=True, server_default=text("'0'"))
    meta_key = Column(String(255), index=True)
    meta_value = Column(String)


class WpUser(Base):
    __tablename__ = u'wp_users'

    ID = Column(BigInteger, primary_key=True)
    user_login = Column(String(60), nullable=False, index=True, server_default=text("''"))
    user_pass = Column(String(64), nullable=False, server_default=text("''"))
    user_nicename = Column(String(50), nullable=False, index=True, server_default=text("''"))
    user_email = Column(String(100), nullable=False, server_default=text("''"))
    user_url = Column(String(100), nullable=False, server_default=text("''"))
    user_registered = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    user_activation_key = Column(String(60), nullable=False, server_default=text("''"))
    user_status = Column(Integer, nullable=False, server_default=text("'0'"))
    display_name = Column(String(250), nullable=False, server_default=text("''"))

