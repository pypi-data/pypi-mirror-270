from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import uuid


class OmnivoreQL:
    def __init__(self, api_token: str, graphql_endpoint_url: str = "https://api-prod.omnivore.app/api/graphql") -> None:
        """
        Initialize a new instance of the GraphQL client.

        :param api_token: The API token to use for authentication.
        :param graphql_endpoint_url: The URL of the Omnivore GraphQL endpoint.
        """
        transport = RequestsHTTPTransport(
            url=graphql_endpoint_url,
            headers={"content-type": "application/json", "authorization": api_token},
            use_json=True,
        )
        self.client = Client(transport=transport,
                             fetch_schema_from_transport=False)

    def save_url(self, url: str):
        """
        Save a URL to Omnivore.

        :param url: The URL to save.
        """
        mutation = gql(
            """
            mutation {
                saveUrl(input: { clientRequestId: "%s", source: "api", url: "%s" }) {
                    ... on SaveSuccess {
                        url
                        clientRequestId
                    }
                    ... on SaveError {
                        errorCodes
                        message
                    }
                }
            }
        """
            % (uuid.uuid4(), url)
        )
        return self.client.execute(mutation)

    def save_page(self, url: str, original_content: str):
        """
        Save a page with html content to Omnivore.

        :param url: The URL of the page to save.
        :param original_content: The original html content of the page.
        """
        mutation = gql(
            """
            mutation {
                savePage(input: { clientRequestId: "%s", source: "api", url: "%s", originalContent:"%s" }) {
                    ... on SaveSuccess {
                        url
                        clientRequestId
                    }
                    ... on SaveError {
                        errorCodes
                        message
                    }
                }
            }
        """
            % (uuid.uuid4(), url, original_content)
        )
        return self.client.execute(mutation)

    def get_profile(self):
        """
        Get the profile of the current user.
        """
        query = gql(
            """
            query Viewer {
            me {
                id
                name
                isFullUser
                profile {
                id
                username
                pictureUrl
                bio
                }
            }
            }
        """
        )
        return self.client.execute(query)

    def get_labels(self):
        """
        Get the labels of the current user.
        """
        query = gql(
            """
            query GetLabels { 
                labels {
                    ... on LabelsSuccess {
                    labels {
                        ...LabelFields
                    }
                    }
                    ... on LabelsError {
                    errorCodes
                    }
                }
            }
            fragment LabelFields on Label {
                id
                name
                color
                description
                createdAt
            }"""
        )
        return self.client.execute(query)

    def get_subscriptions(self):
        """
        Get the subscriptions of the current user.
        """
        query = gql(
            """
                query GetSubscriptions {
                subscriptions(sort: { by: UPDATED_TIME }) {
                    ... on SubscriptionsSuccess {
                    subscriptions {
                        id
                        name
                        newsletterEmail
                        url
                        description
                        status
                        unsubscribeMailTo
                        unsubscribeHttpUrl
                        createdAt
                        updatedAt
                    }
                    }
                    ... on SubscriptionsError {
                    errorCodes
                    }
                }
                }
            """
        )
        return self.client.execute(query)

    def get_articles(self, limit: int = None, cursor: str = None, format: str = 'markdown', query: str = "in:inbox", include_content: bool = False):
        """
        Get articles for the current user.

        :param limit: The number of articles to return.
        :param cursor: The cursor to use for pagination.
        :param format: The format of the articles to return.
        :param query: The query to use for filtering articles. Example of query by date: 'in:inbox published:2024-03-01..*'. See https://docs.omnivore.app/using/search.html#filtering-by-save-publish-dates for more information.
        :param include_content: Whether to include the content of the articles.
        """
        q = gql(
            """
            query Search($after: String, $first: Int, $query: String, $format: String, $includeContent: Boolean) {
                search(after: $after, first: $first, query: $query, format: $format, includeContent: $includeContent) {
                    ... on SearchSuccess {
                        edges {
                            cursor
                            node {
                                id
                                title
                                slug
                                url
                                pageType
                                contentReader
                                createdAt
                                isArchived
                                readingProgressPercent
                                readingProgressTopPercent
                                readingProgressAnchorIndex
                                author
                                image
                                description
                                publishedAt
                                ownedByViewer
                                originalArticleUrl
                                uploadFileId
                                labels {
                                    id
                                    name
                                    color
                                }
                                pageId
                                shortId
                                quote
                                annotation
                                state
                                siteName
                                subscription
                                readAt
                                savedAt
                                wordsCount
                                recommendations {
                                    id
                                    name
                                    note
                                    user {
                                        userId
                                        name
                                        username
                                        profileImageURL
                                    }
                                    recommendedAt
                                }
                                highlights {
                                    ...HighlightFields
                                }
                            }
                        }
                        pageInfo {
                            hasNextPage
                            hasPreviousPage
                            startCursor
                            endCursor
                            totalCount
                        }
                    }
                    ... on SearchError {
                        errorCodes
                    }
                }
            }
            
            fragment HighlightFields on Highlight {
                id
                type
                shortId
                quote
                prefix
                suffix
                patch
                annotation
                createdByMe
                createdAt
                updatedAt
                sharedAt
                highlightPositionPercent
                highlightPositionAnchorIndex
                labels {
                    id
                    name
                    color
                    createdAt
                }
            }
        """
        )
        return self.client.execute(
            q, variable_values={
                "first": limit, "after": cursor, "query": query, "format": format, "includeContent": include_content}
        )

    def get_article(self, username: str, slug: str, format: str = None):
        """
        Get an article by username and slug.

        :param username: Omnivore username.
        :param slug: The slug of the article.
        :param format: The format of the article to return.
        """
        query = gql(
            """
            query GetArticle($username: String!, $slug: String!, $format: String, $includeFriendsHighlights: Boolean) {
                article(username: $username, slug: $slug, format: $format) {
                    ... on ArticleSuccess {
                        article {
                            ...ArticleFields
                            content
                            highlights(input: { includeFriends: $includeFriendsHighlights }) {
                                ...HighlightFields
                            }
                            labels {
                                ...LabelFields
                            }
                            recommendations {
                                ...RecommendationFields
                            }
                        }
                    }
                    ... on ArticleError {
                        errorCodes
                    }
                }
            }
            
            fragment ArticleFields on Article {
                id
                title
                url
                author
                image
                savedAt
                createdAt
                publishedAt
                contentReader
                originalArticleUrl
                readingProgressPercent
                readingProgressTopPercent
                readingProgressAnchorIndex
                slug
                isArchived
                description
                linkId
                state
                wordsCount
            }

            fragment HighlightFields on Highlight {
                id
                type
                shortId
                quote
                prefix
                suffix
                patch
                annotation
                createdByMe
                createdAt
                updatedAt
                sharedAt
                highlightPositionPercent
                highlightPositionAnchorIndex
                labels {
                    id
                    name
                    color
                    createdAt
                }
            }

            fragment LabelFields on Label {
                id
                name
                color
                description
                createdAt
            }

            fragment RecommendationFields on Recommendation {
                id
                name
                note
                user {
                    userId
                    name
                    username
                    profileImageURL
                }
                recommendedAt
            }
        """
        )
        return self.client.execute(
            query,
            variable_values={
                "username": username,
                "slug": slug,
                "format": format,
            },
        )

    def archive_article(self, article_id: str, to_archive: bool = True):
        """
        Archive or unarchive an article.

        :param article_id: The ID of the article to archive.
        :param to_archive: Whether to archive or unarchive the article.
        """
        mutation = gql(
            """
        mutation SetLinkArchived($input: ArchiveLinkInput!) {
            setLinkArchived(input: $input) {
                    ... on ArchiveLinkSuccess {
                        linkId
                        message
                    }
                    ... on ArchiveLinkError {
                        errorCodes
                        message
                    }
                }
            }
        """)
        return self.client.execute(
            mutation,
            variable_values={"input": {"linkId": article_id, "archived": to_archive}},
        )

    def unarchive_article(self, article_id: str):
        """
        Unarchive an article.

        :param article_id: The ID of the article to unarchive.
        """
        return self.archive_article(article_id, False)

    def delete_article(self, article_id: str):
        """
        Delete an article.

        :param article_id: The ID of the article to delete.
        """
        mutation = gql("""
            mutation SetBookmarkArticle($input: SetBookmarkArticleInput!) {
                setBookmarkArticle(input: $input) {
                    ... on SetBookmarkArticleSuccess {
                        bookmarkedArticle {
                            id
                        }
                    }
                    ... on SetBookmarkArticleError {
                        errorCodes
                    }
                }
            }""")
        return self.client.execute(
            mutation,
            variable_values= {
                "input": {
                    "articleID": article_id,
                    "bookmark": False
                }
            }
        )
