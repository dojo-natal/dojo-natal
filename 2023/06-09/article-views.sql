-- https://leetcode.com/problems/article-views-i/
# Write your MySQL query statement below
select distinct author_id as id from Views
where author_id = viewer_id
order by author_id asc
