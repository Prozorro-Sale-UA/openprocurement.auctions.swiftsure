# -*- coding: utf-8 -*-
from openprocurement.auctions.core.utils import (
    opresource
)
from openprocurement.auctions.core.plugins.awarding_2_0.views.award import (
    AuctionAwardResource as BaseAuctionAwardResource
)


@opresource(name='dgfOtherAssets:Auction Awards',
            collection_path='/auctions/{auction_id}/awards',
            path='/auctions/{auction_id}/awards/{award_id}',
            auctionsprocurementMethodType="dgfOtherAssets",
            description="Auction awards")
class AuctionAwardResource(BaseAuctionAwardResource):
    pass
