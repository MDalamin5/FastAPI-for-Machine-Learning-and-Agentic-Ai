-- Final Corrected Dummy Data for a Blog Application
-- Removed invalid prefixes from all UUIDs.

-- 1️⃣ Users Table (15 rows)
INSERT INTO "user" (id, username, email, created_at) VALUES
('8a1b5c2d-9e3f-4a6b-8c7d-0e1f2a3b4c5d', 'john_doe', 'john.doe@example.com', '2025-01-10 10:00:00'),
('7b2c6d3e-8f4a-4b7c-9d8e-1f2a3b4c5d6e', 'jane_smith', 'jane.smith@example.com', '2025-01-11 11:30:00'),
('6c3d7e4f-7a5b-4c8d-ae9f-2a3b4c5d6e7f', 'alice_jones', 'alice.jones@example.com', '2025-02-15 09:00:00'),
('5d4e8f5a-6b6c-4d9e-bf0a-3b4c5d6e7f8a', 'bob_brown', 'bob.brown@example.com', '2025-02-20 14:00:00'),
('4e5f9a6b-5c7d-4e0f-a01b-4c5d6e7f8a9b', 'charlie_davis', 'charlie.davis@example.com', '2025-03-05 16:45:00'),
('3f6a0b7c-4d8e-4f1a-b12c-5d6e7f8a9b0c', 'diana_miller', 'diana.miller@example.com', '2025-03-12 18:20:00'),
('2a7b1c8d-3e9f-4a2b-c23d-6e7f8a9b0c1d', 'frank_white', 'frank.white@example.com', '2025-04-01 08:00:00'),
('1b8c2d9e-2f0a-4b3c-d34e-7f8a9b0c1d2e', 'grace_hall', 'grace.hall@example.com', '2025-04-10 12:10:00'),
('9c9d3e0f-1a1b-4c4d-e45f-8a9b0c1d2e3f', 'henry_king', 'henry.king@example.com', '2025-05-22 22:00:00'),
('8d0e4f1a-0b2c-4d5e-f56a-9b0c1d2e3f4a', 'irene_lopez', 'irene.lopez@example.com', '2025-06-14 13:30:00'),
('7e1f5a2b-9c3d-4e6f-a67b-0c1d2e3f4a5b', 'jack_martin', 'jack.martin@example.com', '2025-07-07 07:45:00'),
('6f2a6b3c-8d4e-4f7a-b78c-1d2e3f4a5b6c', 'karen_scott', 'karen.scott@example.com', '2025-08-19 19:00:00'),
('5a3b7c4d-7e5f-4a8b-c89d-2e3f4a5b6c7d', 'leo_turner', 'leo.turner@example.com', '2025-09-01 11:55:00'),
('4b4c8d5e-6f6a-4b9c-d90e-3f4a5b6c7d8e', 'mia_clark', 'mia.clark@example.com', '2025-10-10 10:10:00'),
('3c5d9e6f-5a7b-4cac-ea1f-4a5b6c7d8e9f', 'noah_lewis', 'noah.lewis@example.com', '2025-10-15 15:15:00');

-- 2️⃣ Profile Table (15 rows)
INSERT INTO profile (id, bio, website, user_id) VALUES
('a1a1a1a1-b1b1-41c1-81d1-000000000001', 'Software developer and tech enthusiast.', 'https://johndoe.com', '8a1b5c2d-9e3f-4a6b-8c7d-0e1f2a3b4c5d'),
('a2a2a2a2-b2b2-42c2-82d2-000000000002', 'Data scientist and blogger.', 'https://janesmith.io', '7b2c6d3e-8f4a-4b7c-9d8e-1f2a3b4c5d6e'),
('a3a3a3a3-b3b3-43c3-83d3-000000000003', 'Cloud engineer specializing in AWS.', 'https://alicejones.cloud', '6c3d7e4f-7a5b-4c8d-ae9f-2a3b4c5d6e7f'),
('a4a4a4a4-b4b4-44c4-84d4-000000000004', 'Frontend developer with a passion for UX/UI.', 'https://bobbrown.dev', '5d4e8f5a-6b6c-4d9e-bf0a-3b4c5d6e7f8a'),
('a5a5a5a5-b5b5-45c5-85d5-000000000005', 'Full-stack developer and open-source contributor.', NULL, '4e5f9a6b-5c7d-4e0f-a01b-4c5d6e7f8a9b'),
('a6a6a6a6-b6b6-46c6-86d6-000000000006', 'Cybersecurity expert and author.', 'https://dianamiller.secure', '3f6a0b7c-4d8e-4f1a-b12c-5d6e7f8a9b0c'),
('a7a7a7a7-b7b7-47c7-87d7-000000000007', 'Lover of clean code and agile methodologies.', 'https://frankwhite.codes', '2a7b1c8d-3e9f-4a2b-c23d-6e7f8a9b0c1d'),
('a8a8a8a8-b8b8-48c8-88d8-000000000008', 'Database administrator for large-scale systems.', NULL, '1b8c2d9e-2f0a-4b3c-d34e-7f8a9b0c1d2e'),
('a9a9a9a9-b9b9-49c9-89d9-000000000009', 'Machine learning engineer focused on NLP.', 'https://henryking.ai', '9c9d3e0f-1a1b-4c4d-e45f-8a9b0c1d2e3f'),
('b1b1b1b1-c1c1-41d1-91e1-000000000010', 'Mobile app developer for iOS and Android.', 'https://irenelopez.apps', '8d0e4f1a-0b2c-4d5e-f56a-9b0c1d2e3f4a'),
('b2b2b2b2-c2c2-42d2-92e2-000000000011', 'DevOps specialist transforming development pipelines.', 'https://jackmartin.devops', '7e1f5a2b-9c3d-4e6f-a67b-0c1d2e3f4a5b'),
('b3b3b3b3-c3c3-43d3-93e3-000000000012', 'Technical writer and documentation expert.', NULL, '6f2a6b3c-8d4e-4f7a-b78c-1d2e3f4a5b6c'),
('b4b4b4b4-c4c4-44d4-94e4-000000000013', 'Game developer working with Unity and C#.', 'https://leoturner.games', '5a3b7c4d-7e5f-4a8b-c89d-2e3f4a5b6c7d'),
('b5b5b5b5-c5c5-45d5-95e5-000000000014', 'Product Manager with a technical background.', 'https://miaclark.pm', '4b4c8d5e-6f6a-4b9c-d90e-3f4a5b6c7d8e'),
('b6b6b6b6-c6c6-46d6-96e6-000000000015', 'QA Engineer passionate about automation testing.', NULL, '3c5d9e6f-5a7b-4cac-ea1f-4a5b6c7d8e9f');

-- 3️⃣ Tag Table (15 rows)
INSERT INTO tag (id, name) VALUES
('11111111-1111-4111-8111-000000000001', 'Technology'),
('11111111-1111-4111-8111-000000000002', 'Programming'),
('11111111-1111-4111-8111-000000000003', 'Data Science'),
('11111111-1111-4111-8111-000000000004', 'Machine Learning'),
('11111111-1111-4111-8111-000000000005', 'Web Development'),
('11111111-1111-4111-8111-000000000006', 'Python'),
('11111111-1111-4111-8111-000000000007', 'JavaScript'),
('11111111-1111-4111-8111-000000000008', 'Cloud Computing'),
('11111111-1111-4111-8111-000000000009', 'Security'),
('11111111-1111-4111-8111-000000000010', 'DevOps'),
('11111111-1111-4111-8111-000000000011', 'Career'),
('11111111-1111-4111-8111-000000000012', 'Tutorial'),
('11111111-1111-4111-8111-000000000013', 'Productivity'),
('11111111-1111-4111-8111-000000000014', 'Databases'),
('11111111-1111-4111-8111-000000000015', 'Software Architecture');

-- 4️⃣ BlogPost Table (20 rows)
INSERT INTO blogpost (id, title, content, published_at, user_id) VALUES
('22222222-2222-4222-8222-000000000001', 'The Future of AI', 'Exploring the advancements in artificial intelligence...', '2025-02-01 12:00:00', '8a1b5c2d-9e3f-4a6b-8c7d-0e1f2a3b4c5d'),
('22222222-2222-4222-8222-000000000002', 'A Guide to Python', 'A comprehensive guide to getting started with Python programming.', '2025-02-10 15:30:00', '7b2c6d3e-8f4a-4b7c-9d8e-1f2a3b4c5d6e'),
('22222222-2222-4222-8222-000000000003', 'Data Visualization Techniques', 'Learn how to create compelling data visualizations.', '2025-03-11 09:45:00', '8a1b5c2d-9e3f-4a6b-8c7d-0e1f2a3b4c5d'),
('22222222-2222-4222-8222-000000000004', 'Understanding Docker and Containers', 'An introduction to containerization with Docker.', '2025-03-20 11:00:00', '4e5f9a6b-5c7d-4e0f-a01b-4c5d6e7f8a9b'),
('22222222-2222-4222-8222-000000000005', 'REST APIs vs. GraphQL', 'A deep dive into the pros and cons of each API architecture.', '2025-04-05 14:00:00', '5d4e8f5a-6b6c-4d9e-bf0a-3b4c5d6e7f8a'),
('22222222-2222-4222-8222-000000000006', 'Mastering SQL Joins', 'Everything you need to know about INNER, LEFT, RIGHT, and FULL OUTER joins.', '2025-04-15 18:00:00', '1b8c2d9e-2f0a-4b3c-d34e-7f8a9b0c1d2e'),
('22222222-2222-4222-8222-000000000007', 'Getting Started with React Hooks', 'A tutorial for developers moving from class components.', '2025-05-02 10:20:00', '5d4e8f5a-6b6c-4d9e-bf0a-3b4c5d6e7f8a'),
('22222222-2222-4222-8222-000000000008', 'Building a CI/CD Pipeline with Jenkins', 'Step-by-step guide to automate your workflow.', '2025-05-25 16:00:00', '7e1f5a2b-9c3d-4e6f-a67b-0c1d2e3f4a5b'),
('22222222-2222-4222-8222-000000000009', 'Top 10 Cybersecurity Threats in 2025', 'How to protect your systems from emerging threats.', '2025-06-10 09:00:00', '3f6a0b7c-4d8e-4f1a-b12c-5d6e7f8a9b0c'),
('22222222-2222-4222-8222-000000000010', 'Why I Chose a Career in Tech', 'A personal story and advice for aspiring developers.', '2025-06-20 13:15:00', '2a7b1c8d-3e9f-4a2b-c23d-6e7f8a9b0c1d'),
('22222222-2222-4222-8222-000000000011', 'Natural Language Processing with Transformers', 'An overview of the BERT and GPT models.', '2025-07-01 11:30:00', '9c9d3e0f-1a1b-4c4d-e45f-8a9b0c1d2e3f'),
('22222222-2222-4222-8222-000000000012', 'How to Be More Productive as a Developer', 'Tips and tricks to improve your focus and workflow.', '2025-07-15 19:00:00', '5a3b7c4d-7e5f-4a8b-c89d-2e3f4a5b6c7d'),
('22222222-2222-4222-8222-000000000013', 'Introduction to Serverless Architecture', 'Moving beyond traditional servers with AWS Lambda.', '2025-08-05 10:00:00', '6c3d7e4f-7a5b-4c8d-ae9f-2a3b4c5d6e7f'),
('22222222-2222-4222-8222-000000000014', 'Scaling Your Application with Microservices', 'The benefits and challenges of a microservice architecture.', '2025-08-22 14:45:00', '3c5d9e6f-5a7b-4cac-ea1f-4a5b6c7d8e9f'),
('22222222-2222-4222-8222-000000000015', 'My Favorite VS Code Extensions', 'A curated list of extensions for web developers.', '2025-09-10 12:00:00', '4b4c8d5e-6f6a-4b9c-d90e-3f4a5b6c7d8e'),
('22222222-2222-4222-8222-000000000016', 'What is SQL Injection and How to Prevent It', 'A crucial topic for every developer.', '2025-09-18 17:00:00', '3f6a0b7c-4d8e-4f1a-b12c-5d6e7f8a9b0c'),
('22222222-2222-4222-8222-000000000017', 'Thinking in Algorithms', 'Improving your problem-solving skills.', '2025-10-02 08:30:00', '8a1b5c2d-9e3f-4a6b-8c7d-0e1f2a3b4c5d'),
('22222222-2222-4222-8222-000000000018', 'Managing State in a Large React Application', 'Comparing Redux, MobX, and Context API.', '2025-10-05 11:10:00', '5d4e8f5a-6b6c-4d9e-bf0a-3b4c5d6e7f8a'),
('22222222-2222-4222-8222-000000000019', 'The Importance of Clean Code', 'Why writing readable and maintainable code matters.', '2025-10-12 15:00:00', '2a7b1c8d-3e9f-4a2b-c23d-6e7f8a9b0c1d'),
('22222222-2222-4222-8222-000000000020', 'A Beginner''s Guide to Kubernetes', 'Orchestrating containers at scale.', '2025-10-18 10:00:00', '7e1f5a2b-9c3d-4e6f-a67b-0c1d2e3f4a5b');


-- 5️⃣ PostTagLink Table (Many-to-Many relationships)
INSERT INTO posttaglink (post_id, tag_id) VALUES
-- Post 1
('22222222-2222-4222-8222-000000000001', '11111111-1111-4111-8111-000000000001'),
('22222222-2222-4222-8222-000000000001', '11111111-1111-4111-8111-000000000003'),
('22222222-2222-4222-8222-000000000001', '11111111-1111-4111-8111-000000000004'),
-- Post 2
('22222222-2222-4222-8222-000000000002', '11111111-1111-4111-8111-000000000002'),
('22222222-2222-4222-8222-000000000002', '11111111-1111-4111-8111-000000000006'),
('22222222-2222-4222-8222-000000000002', '11111111-1111-4111-8111-000000000012'),
-- Post 3
('22222222-2222-4222-8222-000000000003', '11111111-1111-4111-8111-000000000003'),
('22222222-2222-4222-8222-000000000003', '11111111-1111-4111-8111-000000000012'),
-- Post 4
('22222222-2222-4222-8222-000000000004', '11111111-1111-4111-8111-000000000001'),
('22222222-2222-4222-8222-000000000004', '11111111-1111-4111-8111-000000000010'),
('22222222-2222-4222-8222-000000000004', '11111111-1111-4111-8111-000000000012'),
-- Post 5
('22222222-2222-4222-8222-000000000005', '11111111-1111-4111-8111-000000000005'),
('22222222-2222-4222-8222-000000000005', '11111111-1111-4111-8111-000000000015'),
-- Post 6
('22222222-2222-4222-8222-000000000006', '11111111-1111-4111-8111-000000000002'),
('22222222-2222-4222-8222-000000000006', '11111111-1111-4111-8111-000000000014'),
('22222222-2222-4222-8222-000000000006', '11111111-1111-4111-8111-000000000012'),
-- Post 7
('22222222-2222-4222-8222-000000000007', '11111111-1111-4111-8111-000000000005'),
('22222222-2222-4222-8222-000000000007', '11111111-1111-4111-8111-000000000007'),
('22222222-2222-4222-8222-000000000007', '11111111-1111-4111-8111-000000000012'),
-- Post 8
('22222222-2222-4222-8222-000000000008', '11111111-1111-4111-8111-000000000010'),
('22222222-2222-4222-8222-000000000008', '11111111-1111-4111-8111-000000000008'),
-- Post 9
('22222222-2222-4222-8222-000000000009', '11111111-1111-4111-8111-000000000009'),
-- Post 10
('22222222-2222-4222-8222-000000000010', '11111111-1111-4111-8111-000000000011'),
-- Post 11
('22222222-2222-4222-8222-000000000011', '11111111-1111-4111-8111-000000000003'),
('22222222-2222-4222-8222-000000000011', '11111111-1111-4111-8111-000000000004'),
-- Post 12
('22222222-2222-4222-8222-000000000012', '11111111-1111-4111-8111-000000000013'),
('22222222-2222-4222-8222-000000000012', '11111111-1111-4111-8111-000000000011'),
-- Post 13
('22222222-2222-4222-8222-000000000013', '11111111-1111-4111-8111-000000000008'),
('22222222-2222-4222-8222-000000000013', '11111111-1111-4111-8111-000000000015'),
-- Post 14
('22222222-2222-4222-8222-000000000014', '11111111-1111-4111-8111-000000000015'),
('22222222-2222-4222-8222-000000000014', '11111111-1111-4111-8111-000000000010'),
-- Post 15
('22222222-2222-4222-8222-000000000015', '11111111-1111-4111-8111-000000000013'),
('22222222-2222-4222-8222-000000000015', '11111111-1111-4111-8111-000000000001'),
-- Post 16
('22222222-2222-4222-8222-000000000016', '11111111-1111-4111-8111-000000000009'),
('22222222-2222-4222-8222-000000000016', '11111111-1111-4111-8111-000000000014'),
('22222222-2222-4222-8222-000000000016', '11111111-1111-4111-8111-000000000002'),
-- Post 17
('22222222-2222-4222-8222-000000000017', '11111111-1111-4111-8111-000000000002'),
('22222222-2222-4222-8222-000000000017', '11111111-1111-4111-8111-000000000011'),
-- Post 18
('22222222-2222-4222-8222-000000000018', '11111111-1111-4111-8111-000000000005'),
('22222222-2222-4222-8222-000000000018', '11111111-1111-4111-8111-000000000007'),
('22222222-2222-4222-8222-000000000018', '11111111-1111-4111-8111-000000000015'),
-- Post 19
('22222222-2222-4222-8222-000000000019', '11111111-1111-4111-8111-000000000002'),
('22222222-2222-4222-8222-000000000019', '11111111-1111-4111-8111-000000000013'),
-- Post 20
('22222222-2222-4222-8222-000000000020', '11111111-1111-4111-8111-000000000010'),
('22222222-2222-4222-8222-000000000020', '11111111-1111-4111-8111-000000000008'),
('22222222-2222-4222-8222-000000000020', '11111111-1111-4111-8111-000000000001');