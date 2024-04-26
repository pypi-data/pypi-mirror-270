# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

__all__ = (
    "ActivityCityInfo",
    "ActivityCountryInfo",
    "ActivityIdInfo",
    "ActivityRatingInfo",
    "ActivityStateInfo",
    "AdAssetPolicySummary",
    "AdCallToActionAsset",
    "AdDiscoveryCarouselCardAsset",
    "AdImageAsset",
    "AdMediaBundleAsset",
    "AdScheduleInfo",
    "AdTextAsset",
    "AdVideoAsset",
    "AddressInfo",
    "AffiliateLocationFeedItem",
    "AgeDimension",
    "AgeRangeInfo",
    "AgeSegment",
    "AppAdInfo",
    "AppEngagementAdInfo",
    "AppFeedItem",
    "AppPaymentModelInfo",
    "AppPreRegistrationAdInfo",
    "AssetDisapproved",
    "AssetInteractionTarget",
    "AssetLinkPrimaryStatusDetails",
    "AssetUsage",
    "AudienceDimension",
    "AudienceExclusionDimension",
    "AudienceInfo",
    "AudienceSegment",
    "AudienceSegmentDimension",
    "BasicUserListInfo",
    "BookOnGoogleAsset",
    "BrandInfo",
    "BrandListInfo",
    "BudgetCampaignAssociationStatus",
    "BudgetSimulationPoint",
    "BudgetSimulationPointList",
    "BusinessNameFilter",
    "BusinessProfileBusinessNameFilter",
    "BusinessProfileLocation",
    "BusinessProfileLocationGroup",
    "BusinessProfileLocationSet",
    "CallAdInfo",
    "CallAsset",
    "CallFeedItem",
    "CallToActionAsset",
    "CalloutAsset",
    "CalloutFeedItem",
    "CarrierInfo",
    "ChainFilter",
    "ChainLocationGroup",
    "ChainSet",
    "ClickLocation",
    "CombinedAudienceInfo",
    "Commission",
    "ConceptGroup",
    "Consent",
    "ContentLabelInfo",
    "CpcBidSimulationPoint",
    "CpcBidSimulationPointList",
    "CpvBidSimulationPoint",
    "CpvBidSimulationPointList",
    "CriterionCategoryAvailability",
    "CriterionCategoryChannelAvailability",
    "CriterionCategoryLocaleAvailability",
    "CrmBasedUserListInfo",
    "CustomAffinityInfo",
    "CustomAudienceInfo",
    "CustomAudienceSegment",
    "CustomIntentInfo",
    "CustomParameter",
    "CustomerMatchUserListMetadata",
    "CustomizerValue",
    "DateRange",
    "DemandGenProductAdInfo",
    "DetailedDemographicSegment",
    "DeviceInfo",
    "DiscoveryCarouselAdInfo",
    "DiscoveryCarouselCardAsset",
    "DiscoveryMultiAssetAdInfo",
    "DiscoveryVideoResponsiveAdInfo",
    "DisplayUploadAdInfo",
    "DynamicAffiliateLocationSetFilter",
    "DynamicBusinessProfileLocationGroupFilter",
    "DynamicCustomAsset",
    "DynamicEducationAsset",
    "DynamicFlightsAsset",
    "DynamicHotelsAndRentalsAsset",
    "DynamicJobsAsset",
    "DynamicLocalAsset",
    "DynamicLocationSetFilter",
    "DynamicRealEstateAsset",
    "DynamicTravelAsset",
    "EnhancedCpc",
    "EventAttribute",
    "EventItemAttribute",
    "ExclusionSegment",
    "ExpandedDynamicSearchAdInfo",
    "ExpandedTextAdInfo",
    "FinalAppUrl",
    "FlexibleRuleOperandInfo",
    "FlexibleRuleUserListInfo",
    "FrequencyCapEntry",
    "FrequencyCapKey",
    "GenderDimension",
    "GenderInfo",
    "GeoPointInfo",
    "HistoricalMetricsOptions",
    "HotelAdInfo",
    "HotelAdvanceBookingWindowInfo",
    "HotelCalloutAsset",
    "HotelCalloutFeedItem",
    "HotelCheckInDateRangeInfo",
    "HotelCheckInDayInfo",
    "HotelCityInfo",
    "HotelClassInfo",
    "HotelCountryRegionInfo",
    "HotelDateSelectionTypeInfo",
    "HotelIdInfo",
    "HotelLengthOfStayInfo",
    "HotelPropertyAsset",
    "HotelStateInfo",
    "HouseholdIncomeDimension",
    "ImageAdInfo",
    "ImageAsset",
    "ImageDimension",
    "ImageFeedItem",
    "InFeedVideoAdInfo",
    "IncomeRangeInfo",
    "InteractionTypeInfo",
    "IpBlockInfo",
    "ItemAttribute",
    "Keyword",
    "KeywordAnnotations",
    "KeywordConcept",
    "KeywordInfo",
    "KeywordPlanAggregateMetricResults",
    "KeywordPlanAggregateMetrics",
    "KeywordPlanDeviceSearches",
    "KeywordPlanHistoricalMetrics",
    "KeywordThemeInfo",
    "LanguageInfo",
    "LeadFormAsset",
    "LeadFormCustomQuestionField",
    "LeadFormDeliveryMethod",
    "LeadFormField",
    "LeadFormSingleChoiceAnswers",
    "LegacyAppInstallAdInfo",
    "LegacyResponsiveDisplayAdInfo",
    "LifeEventSegment",
    "LifecycleGoalValueSettings",
    "ListingDimensionInfo",
    "ListingDimensionPath",
    "ListingGroupInfo",
    "ListingScopeInfo",
    "LocalAdInfo",
    "LocalServiceIdInfo",
    "LocalServicesDocumentReadOnly",
    "LocationAsset",
    "LocationFeedItem",
    "LocationGroupInfo",
    "LocationInfo",
    "LocationSet",
    "LogicalUserListInfo",
    "LogicalUserListOperandInfo",
    "LookalikeUserListInfo",
    "ManualCpa",
    "ManualCpc",
    "ManualCpm",
    "ManualCpv",
    "MapsLocationInfo",
    "MapsLocationSet",
    "MatchingFunction",
    "MaximizeConversionValue",
    "MaximizeConversions",
    "MediaBundleAsset",
    "MetricGoal",
    "Metrics",
    "MobileAppAsset",
    "MobileAppCategoryInfo",
    "MobileApplicationInfo",
    "MobileDeviceInfo",
    "Money",
    "MonthlySearchVolume",
    "NegativeKeywordListInfo",
    "OfflineUserAddressInfo",
    "Operand",
    "OperatingSystemVersionInfo",
    "PageFeedAsset",
    "ParentalStatusDimension",
    "ParentalStatusInfo",
    "PercentCpc",
    "PercentCpcBidSimulationPoint",
    "PercentCpcBidSimulationPointList",
    "PlacementInfo",
    "PolicySummary",
    "PolicyTopicConstraint",
    "PolicyTopicEntry",
    "PolicyTopicEvidence",
    "PolicyValidationParameter",
    "PolicyViolationKey",
    "PriceAsset",
    "PriceFeedItem",
    "PriceOffer",
    "PriceOffering",
    "ProductBrandInfo",
    "ProductCategoryInfo",
    "ProductChannelExclusivityInfo",
    "ProductChannelInfo",
    "ProductConditionInfo",
    "ProductCustomAttributeInfo",
    "ProductGroupingInfo",
    "ProductItemIdInfo",
    "ProductLabelsInfo",
    "ProductLegacyConditionInfo",
    "ProductTypeFullInfo",
    "ProductTypeInfo",
    "PromotionAsset",
    "PromotionFeedItem",
    "ProximityInfo",
    "RealTimeBiddingSetting",
    "ResponsiveDisplayAdControlSpec",
    "ResponsiveDisplayAdInfo",
    "ResponsiveSearchAdInfo",
    "RuleBasedUserListInfo",
    "SearchThemeInfo",
    "SearchVolumeRange",
    "Segments",
    "ShoppingComparisonListingAdInfo",
    "ShoppingLoyalty",
    "ShoppingProductAdInfo",
    "ShoppingSmartAdInfo",
    "SimilarUserListInfo",
    "SitelinkAsset",
    "SitelinkFeedItem",
    "SkAdNetworkSourceApp",
    "SmartCampaignAdInfo",
    "StoreAttribute",
    "StoreSalesMetadata",
    "StoreSalesThirdPartyMetadata",
    "StructuredSnippetAsset",
    "StructuredSnippetFeedItem",
    "TagSnippet",
    "TargetCpa",
    "TargetCpaSimulationPoint",
    "TargetCpaSimulationPointList",
    "TargetCpm",
    "TargetCpmTargetFrequencyGoal",
    "TargetImpressionShare",
    "TargetImpressionShareSimulationPoint",
    "TargetImpressionShareSimulationPointList",
    "TargetRestriction",
    "TargetRestrictionOperation",
    "TargetRoas",
    "TargetRoasSimulationPoint",
    "TargetRoasSimulationPointList",
    "TargetSpend",
    "TargetingSetting",
    "TextAdInfo",
    "TextAsset",
    "TextLabel",
    "TextMessageFeedItem",
    "TopicInfo",
    "TransactionAttribute",
    "TravelAdInfo",
    "UnknownListingDimensionInfo",
    "UrlCollection",
    "UserAttribute",
    "UserData",
    "UserIdentifier",
    "UserInterestInfo",
    "UserInterestSegment",
    "UserListActionInfo",
    "UserListDateRuleItemInfo",
    "UserListInfo",
    "UserListLogicalRuleInfo",
    "UserListNumberRuleItemInfo",
    "UserListRuleInfo",
    "UserListRuleItemGroupInfo",
    "UserListRuleItemInfo",
    "UserListSegment",
    "UserListStringRuleItemInfo",
    "Value",
    "VideoAdInfo",
    "VideoBumperInStreamAdInfo",
    "VideoNonSkippableInStreamAdInfo",
    "VideoOutstreamAdInfo",
    "VideoResponsiveAdInfo",
    "VideoTrueViewInStreamAdInfo",
    "WebhookDelivery",
    "WebpageConditionInfo",
    "WebpageInfo",
    "WebpageSampleInfo",
    "YearMonth",
    "YearMonthRange",
    "YouTubeChannelInfo",
    "YouTubeVideoInfo",
    "YoutubeVideoAsset",
)
